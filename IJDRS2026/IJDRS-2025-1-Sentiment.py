
# 定义分类及其描述 
CLASSIFICATIONS = { 
    "悲伤": "表达哀痛、悲恸、伤心的评论",
    "愤怒": "表达愤怒、气愤、不满的评论",
    "恐惧": "表达担忧、害怕、焦虑的评论",
    "期待": "表达希望、期望、呼吁的评论", 
    "信任": "表达信赖、感激、认可的评论",
    "惊讶": "表达震惊、不可思议的评论",
    "厌恶": "表达反感、嫌弃、鄙视的评论",
    "其他": "无明显情感或难以分类的评论"
}



messages = [
        {"role": "system", "content": """你是一个社交媒体评论分类助手。对于重大事故的评论，请根据主要表达的情感进行分类。注意：
    1. 每条评论只分配最主要的一个情感类别
    2. 优先考虑评论的核心表达而非表面情绪词
    3. 注意识别反讽、比喻等修辞手法"""},
        {"role": "user", "content": "以下是分类及其描述:\n" + "\n".join([f"{k}: {v}" for k, v in CLASSIFICATIONS.items()])},
        {"role": "user", "content": f"请为以下评论分配一个类别，只需回复类别名称:\n{discussion['AF']}"}
    ]

examples = [
    # --- Anger (愤怒) ---
    {"discussion": "校长必须受到严惩！消防安全措施在哪里？", "classification": "愤怒"},
    {"discussion": "学校的保安在哪里？宿舍管理员在哪里？", "classification": "愤怒"},
    {"discussion": "校长应该进监狱。安全规程怎么了？", "classification": "愤怒"},

    # --- Disgust (厌恶) ---
    {"discussion": "现在的老师啊……", "classification": "厌恶"},
    {"discussion": "这群饭桶能做什么？", "classification": "厌恶"},
    {"discussion": "这学校是茅草屋盖的吗？", "classification": "厌恶"},

    # --- Expectation (期待) ---
    {"discussion": "问题太多了，希望这能得到纠正。", "classification": "期待"},
    {"discussion": "祈祷孩子们早日康复。", "classification": "期待"},
    {"discussion": "安全教育必须深入人心！", "classification": "期待"},

    # --- Fear (恐惧) ---
    {"discussion": "这太吓人了！", "classification": "恐惧"},
    {"discussion": "天啊，这太可怕了。", "classification": "恐惧"},
    {"discussion": "我只能想象幸存者们该有多害怕。", "classification": "恐惧"},

    # --- Sadness (悲伤) ---
    {"discussion": "十三个孩子……就是十三个破碎的家庭。", "classification": "悲伤"},
    {"discussion": "十三个孩子代表着十三个破碎的家庭。太悲惨了。", "classification": "悲伤"},
    {"discussion": "生命太脆弱了。", "classification": "悲伤"},

    # --- Surprise (惊讶) ---
    {"discussion": "哇……我震惊了，快哭了。", "classification": "惊讶"},
    {"discussion": "学校里怎么会发生火灾？", "classification": "惊讶"},
    {"discussion": "这太严重了。", "classification": "惊讶"},

    # --- Trust (信任) ---
    {"discussion": "为什么？幸好责任人被控制了。我放心了。", "classification": "信任"},
    {"discussion": "为他们的安全祈祷。", "classification": "信任"},
    {"discussion": "安全必须永远第一。", "classification": "信任"},

    # --- Other (其他) ---
    {"discussion": "这学校需要改个名字。", "classification": "其他"},
    {"discussion": "假新闻。", "classification": "其他"},
    {"discussion": "我们需要更多细节。", "classification": "其他"}
]
