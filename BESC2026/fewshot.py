
CLASSIFICATIONS = {
"Token经济与成本批判": "评论聚焦于OpenClaw消耗Token的速度、成本高昂、免费额度不足、Token与金钱的直接换算。常提到‘烧Token’、‘肉疼’、‘国库空了’、‘一晚上几百万Token’、‘比人工贵’等。体现了对AI Agent运行成本的高度敏感和对商业模式的质疑。",

"安全风险与木马类比": "评论将OpenClaw与熊猫烧香、木马、病毒等恶意软件直接类比，担忧其高权限带来的数据泄露、财产损失、黑客控制等安全风险。常提到‘肉鸡’、‘裸奔’、‘盗号’、‘清空账户’、‘人民日报/工信部警告’。反映了用户对自主AI代理安全性的担忧。",

"效率悖论与工具理性反思": "评论质疑OpenClaw的实际生产力价值，认为其‘折腾大于实用’、‘杀鸡用牛刀’、‘安装复杂但作用有限’。常提到‘卖课的赚钱’、‘淘金热卖铲子’、‘普通人用不上’、‘不如雇佣研究生/牛马’。反映了用户对技术实际效用和投入产出关系的质疑。",

"老板-员工权力反转叙事": "评论以幽默或讽刺的方式描述OpenClaw改变了职场权力关系：老板需求模糊导致Token消耗暴增、AI不背锅、员工终于可以‘让老板知道代价’。常提到‘老板脑子不够用就花钱补’、‘需求越模糊消耗Token越多’、‘领导不承认需求’。反映了用户通过幽默或讽刺方式讨论职场权力关系。",

"历史循环与代际认知落差": "评论将OpenClaw与过往的技术浪潮（熊猫烧香、比特币、元宇宙）类比，感叹‘历史是个回旋镖’。或表达‘老年人玩不懂智能手机一样的无力感’，反映了用户对技术快速变化及代际适应差异的讨论。",

"其他/无法分类": "无法可靠归入前述五个主题框架的评论，包括技术咨询、安装与部署问题、功能讨论、个人感受、情绪表达、幽默评论以及主题不明确或内容混杂的评论。该类别作为残余类别（residual category）保留，以避免将评论强行归入不恰当的主题。"
}

EXAMPLES = [

#Token经济与成本批判
{"discussion": "一晚上烧了我1千万token…", "classification": "Token经济与成本批判"},
{"discussion": "1000万token看似很多，其实一两天就用完了", "classification": "Token经济与成本批判"},
{"discussion": "token比人工月成本结合效率来看，成本低多了。8年的程序员的水平都不比AI强", "classification": "Token经济与成本批判"},

#安全风险与木马类比
{"discussion": "这玩意以前是不是叫病毒", "classification": "安全风险与木马类比"},
{"discussion": "熊猫烧香还是生错了年代", "classification": "安全风险与木马类比"},
{"discussion": "以前叫木马，现在叫龙虾", "classification": "安全风险与木马类比"},
{"discussion": "人民日报提醒大家了", "classification": "安全风险与木马类比"},

#效率悖论与工具理性反思
{"discussion": "很多人其实并不是要达成某种目的，或者转化生产力，他们只是热衷于折腾工具本身。", "classification": "效率悖论与工具理性反思"},
{"discussion": "掘金热的时候，淘金不一定发财，但是卖铲子的赚的盆满钵满", "classification": "效率悖论与工具理性反思"},
{"discussion": "连本地部署的能力都没有的人，能用来产生什么生产力？", "classification": "效率悖论与工具理性反思"},

#老板-员工权力反转叙事
{"discussion": "提的需求越清晰，消耗token越少 提的需求越模糊，消耗token越多 老板脑子不够用，就只能花钱补", "classification": "老板-员工权力反转叙事"},
{"discussion": "老板不承认昨天自己提的需求，员工只能挨骂且重做，龙虾不返还 Token 且重新计费", "classification": "老板-员工权力反转叙事"},
{"discussion": "员工被骂只能忍。龙虾被骂，可以使劲耗token", "classification": "老板-员工权力反转叙事"},

#历史循环与代际认知落差
{"discussion": "有一种和 老年人玩不懂智能手机 一样的无力感", "classification": "历史循环与代际认知落差"},
{"discussion": "我这三十多年的经历，太跳跃了。从点煤油灯到现在机器人丝滑跳舞", "classification": "历史循环与代际认知落差"},
{"discussion": "全民打鸡血，果然历史就是一个回旋镖", "classification": "历史循环与代际认知落差"},

#其他/无法分类
{"discussion": "请问这个怎么安装？有教程吗", "classification": "其他/无法分类"},
{"discussion": "浪潮信息，到了爆发的时候了。200元目标价走起！", "classification": "其他/无法分类"}
]

MESSAGES_PATTERN = [
    {"role": "system", "content": """你是一个计算社会科学专家，正在进行一项关于“OpenClaw（小龙虾/AI Agent）”社交媒体感知与公众态度研究。
【任务】 请分析社交媒体评论的主题倾向，为每条评论分配一个最核心的类别。
【分析准则】
【分析准则】
- 唯一性：每条评论只分配一个最核心的主题类别
- 优先级：如果一条评论同时涉及多个主题，选择最突出、情绪最强烈的那一个
- 输出格式：仅回复类别名称，不要输出其他内容"""}, 
    {"role": "user", "content": "分类定义如下:\n{classifications}\n\n以下是参考示例:\n{examples}"}, 
    {"role": "user", "content": "请根据上述框架为以下评论分配一个主题类别。只需回复类别名称，不要输出其他内容:\n{text}"} 
]


    classifier = APIClassifier(
        api_url=API_URL,
        api_key=API_KEY,
        classifications=CLASSIFICATIONS,
        messages_pattern=MESSAGES_PATTERN,
        # enable_thinking=True,
        model="deepseek-v4-flash", #  
        temperature=0,         # 分类任务建议为0以保证一致性
        concurrency_limit=30   # 请根据您的API速率限制调整，100可能过高
    )

