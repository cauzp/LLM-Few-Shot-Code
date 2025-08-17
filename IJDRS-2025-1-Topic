# 定义分类及其描述 
CLASSIFICATIONS = {  
   "管理责任": "关于学校管理问题和直接责任人的评论",
   "制度归因": "关于体制性问题和监管缺失的评论", 
   "具体质疑": "对具体安全措施提出质疑的评论",
   "政策建议": "提出改进措施和政策建议的评论",
   "事实探寻": "询问和讨论事件具体细节的评论",
   "社会关切": "表达社会层面关注和反思的评论",
   "时空情境": "关注事发时间地点特殊性的评论",
   "其他": "不属于上述类别的评论"
}

messages = [
        {"role": "system", "content": """你是一个社交媒体评论分类助手。对于重大事故的评论，请根据主要表达的主题进行分类。注意：
    1. 每条评论只分配最主要的一个主题类别
    2. 优先考虑评论的核心议题而非表面字眼
    3. 注意评论的语境和整体表达意图"""}, 
        {"role": "user", "content": "以下是分类及其描述:\n" + "\n".join([f"{k}: {v}" for k, v in CLASSIFICATIONS.items()])},
        {"role": "user", "content": f"请为以下评论分配一个类别，只需回复类别名称:\n{discussion['AF']}"}
    ]

examples = [
        # --- Fact-Finding (事实探寻) ---
        {"discussion": "这是什么类型的学校？", "classification": "事实探寻"},
        {"discussion": "起火的最初原因是什么？", "classification": "事实探寻"},
        {"discussion": "宿舍里有多少学生？", "classification": "事实探寻"},
        
        # --- Management Accountability (管理责任) ---
        {"discussion": "宿舍管理员在哪里？", "classification": "管理责任"},
        {"discussion": "校长必须负全责", "classification": "管理责任"},
        {"discussion": "为什么晚上没有工作人员看管？", "classification": "管理责任"},
        
        # --- Policy Recommendations (政策建议) ---
        {"discussion": "所有宿舍强制安装烟雾探测器", "classification": "政策建议"},
        {"discussion": "必须要求定期进行安全检查", "classification": "政策建议"},
        {"discussion": "需要更严格的寄宿学校规定", "classification": "政策建议"},
        
        # --- Safety Concerns (具体质疑) ---
        {"discussion": "消防警报安装了吗？能用吗？", "classification": "具体质疑"},
        {"discussion": "为什么宿舍门是锁着的？", "classification": "具体质疑"},
        {"discussion": "紧急出口在哪里？", "classification": "具体质疑"},
        
        # --- Social Commentary (社会关切) ---
        {"discussion": "今年第二次学校火灾了", "classification": "社会关切"},
        {"discussion": "这显示了教育水平在下降", "classification": "社会关切"},
        {"discussion": "农村学校的风险越来越大", "classification": "社会关切"},
        
        # --- Systemic Attribution (制度归因) ---
        {"discussion": "私立学校的又一悲剧——利益重于安全", "classification": "制度归因"},
        {"discussion": "教育监督的彻底失败", "classification": "制度归因"},
        {"discussion": "学校检查制度存在系统性问题", "classification": "制度归因"},
        
        # --- Temporal Context (时空情境) ---
        {"discussion": "为什么学生们没有放假过年？", "classification": "时空情境"},
        {"discussion": "早该放假了", "classification": "时空情境"},
        {"discussion": "春节前的悲剧性时刻", "classification": "时空情境"},
        
        # --- Other (其他) ---
        {"discussion": "分享新闻", "classification": "其他"},
        {"discussion": "无关评论", "classification": "其他"},
        {"discussion": "混合或不明确的主题", "classification": "其他"}
    ]
