import google.generativeai as genai
import time
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def slow_print(text, delay=0.03):
    """模拟终端打字机输出效果，增加视觉停留时间"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def hermes_monitor_mock():
    slow_print("[System] 启动边缘节点多智能体协同中枢...")
    time.sleep(2)
    slow_print("[Agent: Hermes-Monitor] 初始化环境探针，连接本地 Docker 守护进程...")
    time.sleep(3)
    slow_print("[Agent: Hermes-Monitor] 开始执行例行巡检，当前节点负载: CPU 12%, RAM 68%.")
    time.sleep(2)
    slow_print("[Agent: Hermes-Monitor] 扫描容器组: ['hysteria2-proxy', 'wxread-auto', 'home-assistant']...")
    time.sleep(4)
    slow_print("[Agent: Hermes-Monitor] 状态检查: 'hysteria2-proxy' (Healthy), 'home-assistant' (Healthy).")
    time.sleep(1)
    slow_print("[Agent: Hermes-Monitor] 异常警报: 'wxread-auto' 处于 Exited 状态 (Exit Code 137).")
    time.sleep(3)
    slow_print("[Agent: Hermes-Monitor] 正在提取最后 100 行容器日志与宿主机资源占用切片...")
    time.sleep(4)
    mock_log = "System Error: OOMKilled: true\nMemory usage: 1024MB/1024MB\nTraceback: Memory leak in content parsing loop."
    slow_print(f"[Agent: Hermes-Monitor] 数据提取完成。核心错误片段:\n{mock_log}")
    return mock_log

def gemini_reasoning_agent(error_log):
    slow_print("\n[System] 拦截到系统异常，自动拉起异常分析工作流...")
    time.sleep(2)
    slow_print("[Agent: Gemini-Reasoning] 正在组装上下文数据 (包含环境拓扑、历史运维记录、当前日志)...")
    time.sleep(3)
    slow_print("[Agent: Gemini-Reasoning] 向大语言模型发起长链推理请求...")
    
    prompt = f"""
    你是一个边缘计算节点运维 Agent。分析以下 OOM 日志，判断根因并返回修复策略。
    严格以 JSON 格式输出，包含 root_cause 和 action_command 两个字段。
    日志: {error_log}
    """
    
    try:
        # 实际 API 请求时间约为 3-5 秒
        response = model.generate_content(prompt)
        slow_print("[Agent: Gemini-Reasoning] 接收推理结果。正在解析大模型输出策略...")
        time.sleep(2)
        slow_print(response.text, delay=0.02)
        return response.text
    except Exception as e:
        slow_print(f"API 调用失败: {e}")
        return "{}"

def execution_engine_mock(strategy_data):
    slow_print("\n[System] 安全策略审核通过，移交执行引擎...")
    time.sleep(2)
    slow_print("[Engine: Execution] 步骤 1/3: 备份目标容器当前配置参数...")
    time.sleep(3)
    slow_print("[Engine: Execution] 步骤 2/3: 下发热更新指令 (docker update -m 2048m wxread-auto)...")
    time.sleep(4)
    slow_print("[Engine: Execution] 步骤 3/3: 重启目标容器应用新策略...")
    time.sleep(5)
    slow_print("[Agent: Hermes-Monitor] 回调检测: 'wxread-auto' 运行状态恢复为 Up，内存占用曲线平稳。")
    time.sleep(2)
    slow_print("[System] 故障自愈闭环完成，节点恢复无人值守监控模式。")

if __name__ == "__main__":
    log_data = hermes_monitor_mock()
    strategy_data = gemini_reasoning_agent(log_data)
    execution_engine_mock(strategy_data)
