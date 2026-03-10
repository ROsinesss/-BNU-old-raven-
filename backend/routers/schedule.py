"""
课表路由
"""

from fastapi import APIRouter, Depends, HTTPException

from models.schemas import ScheduleResponse
from services.schedule import fetch_schedule, clear_schedule_cache
from routers.deps import get_current_session

router = APIRouter(prefix="/api", tags=["课表"])


@router.get("/schedule", response_model=ScheduleResponse)
async def get_schedule(year: int = 2025, semester: int = 1,
                       refresh: int = 0,
                       session_info=Depends(get_current_session)):
    """
    获取课表
    
    - year: 学年起始年份，如 2025
    - semester: 0=秋季, 1=春季
    - refresh: 1=强制刷新缓存
    """
    session = session_info["session"]
    student_id = session_info["student_id"]
    
    if refresh:
        clear_schedule_cache(student_id)
    
    result = fetch_schedule(session, student_id=student_id,
                            year=year, semester=semester)
    
    if not result.courses:
        # 可能是 token 过期或无数据
        pass
    
    return result
