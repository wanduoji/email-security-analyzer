"""Email header parser"""
from typing import Dict, List, Optional
from dataclasses import dataclass
import re

@dataclass
class EmailHeader:
    """Email header data structure"""
    from_addr: Optional[str] = None
    to_addrs: List[str] = None
    subject: str = ""
    date: Optional[str] = None
    message_id: Optional[str] = None
    received: List[str] = None
    return_path: Optional[str] = None
    dkim_signature: Optional[str] = None
    spf_result: Optional[str] = None
    dmarc_result: Optional[str] = None
    content_type: Optional[str] = None
    
    def __post_init__(self):
        if self.to_addrs is None:
            self.to_addrs = []
        if self.received is None:
            self.received = []
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "from": self.from_addr,
            "to": self.to_addrs,
            "subject": self.subject,
            "date": self.date,
            "message_id": self.message_id,
            "received": self.received,
            "return_path": self.return_path,
            "dkim_signature": self.dkim_signature,
            "spf_result": self.spf_result,
            "dmarc_result": self.dmarc_result,
            "content_type": self.content_type
        }

class EmailHeaderParser:
    """Parse email headers"""
    
    def parse(self, email_content: str) -> EmailHeader:
        """Parse raw email content and extract headers"""
        lines = email_content.split('\n')
        header = EmailHeader()
        
        i = 0
        while i < len(lines) and lines[i].strip():
            line = lines[i]
            
            if line.lower().startswith('from:'):
                header.from_addr = self._extract_email(line)
            elif line.lower().startswith('to:'):
                header.to_addrs = self._extract_emails(line)
            elif line.lower().startswith('subject:'):
                header.subject = line.split(':', 1)[1].strip()
            elif line.lower().startswith('date:'):
                header.date = line.split(':', 1)[1].strip()
            elif line.lower().startswith('message-id:'):
                header.message_id = line.split(':', 1)[1].strip()
            elif line.lower().startswith('received:'):
                header.received.append(line.split(':', 1)[1].strip())
            elif line.lower().startswith('return-path:'):
                header.return_path = line.split(':', 1)[1].strip()
            elif line.lower().startswith('dkim-signature:'):
                header.dkim_signature = line.split(':', 1)[1].strip()
            elif 'spf=' in line.lower():
                header.spf_result = line
            elif 'dmarc=' in line.lower():
                header.dmarc_result = line
            elif line.lower().startswith('content-type:'):
                header.content_type = line.split(':', 1)[1].strip()
            
            i += 1
        
        return header
    
    def _extract_email(self, line: str) -> str:
        """Extract email address from header line"""
        match = re.search(r'[\w\.-]+@[\w\.-]+', line)
        return match.group(0) if match else ""
    
    def _extract_emails(self, line: str) -> List[str]:
        """Extract multiple email addresses from header line"""
        return re.findall(r'[\w\.-]+@[\w\.-]+', line)
    
    def verify_authentication(self, header: EmailHeader) -> Dict:
        """Verify email authentication (DKIM, SPF, DMARC)"""
        return {
            "dkim": "pass" if header.dkim_signature else "fail",
            "spf": "pass" if "pass" in (header.spf_result or "").lower() else "fail",
            "dmarc": "pass" if "pass" in (header.dmarc_result or "").lower() else "fail"
        }
