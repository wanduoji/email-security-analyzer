"""API routes for email security analyzer"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

# Request/Response models
class AnalyzeRequest(BaseModel):
    email_content: str
    priority: Optional[str] = "accuracy"  # accuracy or speed

class AnalysisResponse(BaseModel):
    task_id: str
    risk_level: str
    is_phishing: bool
    confidence: float
    overall_score: float
    recommendations: List[str]
    model_used: str
    analysis_time: float

# Mock responses for demonstration
@router.post("/analyze", response_model=dict)
async def analyze(request: AnalyzeRequest):
    """
    Perform comprehensive email security analysis using AI models
    - Priority: accuracy (uses Claude 3 Opus)
    - Includes full DKIM/SPF verification, URL analysis, phishing detection
    """
    try:
        if not request.email_content:
            raise HTTPException(status_code=400, detail="email_content cannot be empty")
        
        # Mock analysis result
        return {
            "task_id": "analysis_1719574800000",
            "risk_level": "HIGH",
            "is_phishing": True,
            "confidence": 0.92,
            "overall_score": 82.5,
            "recommendations": [
                "This appears to be a phishing email. Do not click any links.",
                "Report immediately to IT security team."
            ],
            "model_used": "claude-3-opus",
            "analysis_time": 2.34,
            "detections": {
                "phishing_indicators": [
                    {
                        "name": "urgency_language",
                        "description": "Urgent action required detected",
                        "severity": "HIGH",
                        "weight": 0.20
                    }
                ],
                "urls": [
                    {
                        "url": "https://verify-account.tk",
                        "risk_score": 0.85,
                        "risk_level": "HIGH"
                    }
                ]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quick-analyze", response_model=dict)
async def quick_analyze(request: AnalyzeRequest):
    """
    Fast email security analysis using rule-based detection only
    - Priority: speed (uses rule engine)
    - Response time: <500ms
    - Perfect for high-volume screening
    """
    try:
        if not request.email_content:
            raise HTTPException(status_code=400, detail="email_content cannot be empty")
        
        # Mock quick analysis result
        return {
            "task_id": "quick_analysis_1719574800001",
            "risk_level": "MEDIUM",
            "is_phishing": False,
            "confidence": 0.75,
            "overall_score": 45.2,
            "recommendations": [
                "Review this email manually before taking action."
            ],
            "model_used": "rule_engine",
            "analysis_time": 0.23
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/batch-analyze", response_model=dict)
async def batch_analyze(requests: List[AnalyzeRequest]):
    """
    Batch analyze multiple emails
    - Supports up to 100 emails per request
    - Returns results in same order as input
    """
    try:
        if not requests:
            raise HTTPException(status_code=400, detail="requests cannot be empty")
        
        if len(requests) > 100:
            raise HTTPException(status_code=400, detail="Maximum 100 emails per batch")
        
        # Mock batch results
        return {
            "batch_id": "batch_1719574800002",
            "total": len(requests),
            "processed": len(requests),
            "results": [
                {
                    "index": i,
                    "risk_level": "HIGH" if i % 2 == 0 else "LOW",
                    "is_phishing": i % 2 == 0,
                    "overall_score": 85.0 if i % 2 == 0 else 20.0,
                    "analysis_time": 1.5
                }
                for i in range(len(requests))
            ],
            "batch_time": 5.23
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models", response_model=dict)
async def get_models():
    """Get available models and their capabilities"""
    return {
        "models": [
            {
                "name": "claude-3-opus",
                "provider": "anthropic",
                "context_window": 200000,
                "capabilities": [
                    "Email header analysis",
                    "URL risk assessment",
                    "Phishing detection",
                    "Multi-language support"
                ],
                "speed": "Medium",
                "cost": "High"
            },
            {
                "name": "gpt-4-turbo",
                "provider": "openai",
                "context_window": 128000,
                "capabilities": [
                    "Email header analysis",
                    "URL risk assessment",
                    "Vision analysis",
                    "Multi-language support"
                ],
                "speed": "Fast",
                "cost": "Medium"
            },
            {
                "name": "rule_engine",
                "provider": "local",
                "context_window": 1000000,
                "capabilities": [
                    "Rule-based phishing detection",
                    "Pattern matching",
                    "Fast batch processing"
                ],
                "speed": "Very Fast",
                "cost": "None"
            }
        ],
        "routing": {
            "strategy": "smart",
            "description": "Automatically selects best model based on email complexity"
        }
    }
