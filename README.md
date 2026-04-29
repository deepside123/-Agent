# Mi-Ecosystem-Agent: “人车家全生态”智能规划助理

本项目是一个基于 **LangGraph** 和 **MiMo-V2.5-Pro** 构建的高级 Agent，旨在实现小米“人车家全生态”的深度闭环联动。

### 🌟 核心功能
- **复杂意图拆解**：不仅是执行指令，更能根据“明早有雨”自动推理出“今晚关闭米家窗户”并“明早提前15分钟启动小米汽车预热”。
- **长链推理**：利用 MiMo 模型的高性能推理能力，在多个智能节点间进行状态协同。
- **动态博弈**：当车辆续航不足以覆盖日程路线时，Agent 会主动建议充电路径并同步至车载导航。

### 🛠 技术栈
- **Orchestration**: LangGraph (State Machine)
- **Framework**: Python 3.10+
- **Protocol**: 模拟 Miot (米家) 与小米汽车开放接口
- **LLM**: MiMo-V2.5-Pro

### 🚀 运行示例
输入：“我明早九点要在科技园开会，看天气预报明天会降温。”
Agent 自动执行链条：
1. `get_calendar_and_weather` -> 确认行程与气温。
2. `get_mi_home_status` -> 检查家中加湿器与窗户状态。
3. `control_mi_car` -> 预约明早 08:45 开启座舱加热。
