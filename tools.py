import json

def get_mi_home_status(device_name: str):
    """获取米家智能家居状态。参数 device_name: 设备名称如 '空调', '窗户'"""
    # 模拟返回
    return json.dumps({"device": device_name, "status": "on", "mode": "cooling", "temp": 26})

def control_mi_car(action: str, target_temp: int = 22):
    """控制小米汽车（SU7）。action: 'pre_heat' (预热), 'check_range' (检查续航)"""
    if action == "pre_heat":
        return json.dumps({"status": "success", "msg": f"车辆已启动预热，目标温度{target_temp}度"})
    return json.dumps({"battery": "85%", "range": "680km"})

def get_calendar_and_weather():
    """获取用户日程和当地天气"""
    return json.dumps({
        "schedule": "上午9:00 在小米科技园有重要会议",
        "weather": "有雨",
        "outdoor_temp": "12°C"
    })

# 导出工具列表供 Agent 使用
tools = [get_mi_home_status, control_mi_car, get_calendar_and_weather]
