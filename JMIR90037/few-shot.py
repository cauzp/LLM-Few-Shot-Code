import asyncio

CLASSIFICATIONS = {
    "个人经历与现状分享": "评论者分享自身感染HIV后的具体经历、症状、治疗日常、心理状态，或描述视频中人物的（可见）健康状况、生活细节。",
    "担忧、恐惧与焦虑情绪": "评论表达对感染艾滋病的恐惧、对患者处境的担忧、对疾病本身的害怕、对社会歧视的焦虑等负面情绪。",
    "幽默、戏谑与反讽表达": "评论以幽默、调侃、夸张、反讽或戏谑的方式讨论艾滋病或相关话题，可能包含表情符号，可视为一种社会化风险应对或情绪缓解，也可能带有讽刺或不当意味。",
    "疾病知识与传播讨论 (疑问/科普/辟谣)": "评论讨论艾滋病的传播途径、潜伏期、症状、检测方法、预防措施、治疗进展等相关医学知识，包括提问、分享信息、科普、辟谣或表达错误认知。",
    "信息来源与信任度讨论": "评论对有关艾滋病的医学信息、新闻报道（如治愈进展）、专家观点、科普内容或平台信息的准确性、及时性、可靠性进行评价、质疑或确认。",
    "社会影响与公共议题探讨": "评论讨论艾滋病对个人（患者或非患者）的社交、婚恋、家庭、工作、心理健康以及社会层面的影响，包括歧视、污名化、政策建议、公共卫生议题、法律责任等。",
    "风险轻视与认知偏差": "评论轻描淡写感染艾滋病的风险或疾病的严重性，认为“没什么大不了”、“能治好就没事”，对预防措施表示不屑，或对病毒传播力存在错误低估和认知偏差。",
    "支持、鼓励与人文关怀": "评论表达对艾滋病患者的同情、理解、支持、鼓励，祈愿康复或医学进步，呼吁消除歧视、尊重隐私，或分享积极应对的态度。",
    "道德评判与归因指责": "评论对艾滋病感染原因或患者行为进行道德评判，将疾病与特定行为（如性生活方式、吸毒）或人群（如性少数群体、特定职业）污名化联系，表达谴责、指责、歧视或带有偏见的归因。",
    "其他/无法分类": "不属于以上任何明确类别的文本评论，如与艾滋病话题无关的内容、纯粹的情绪宣泄（如单个表情符号且无上下文）、无意义字符或难以判断其核心意图的零散内容。"
}

# 2. 定义示例 (EXAMPLES)
#    从您提供的评论中选取或构造一些清晰的例子。
#    确保 'discussion' 包含评论文本，'classification' 包含对应的 CLASSIFICATIONS 中的中文键名。
EXAMPLES = [
    # 个人经历与现状分享
    {"discussion": "这个HIV的特殊患者，丝毫没有症状", "classification": "个人经历与现状分享"},
    {"discussion": "我这个星期两边屁股 有斑块一样连着一起的痒的不得了 好害怕", "classification": "个人经历与现状分享"},
    {"discussion": "就当慢性病看待，坚持吃药我已经检测不到了，当下是好好挣钱，给自己给家人更好的生活", "classification": "个人经历与现状分享"},
    {"discussion": "1796天，差不多五年", "classification": "个人经历与现状分享"},
    {"discussion": "我朋友终于有救了 我给他", "classification": "个人经历与现状分享"}, # 分享因信息而采取的行动或状态改变

    # 担忧、恐惧与焦虑情绪
    {"discussion": "好可怜，好可怕", "classification": "担忧、恐惧与焦虑情绪"},
    {"discussion": "现在我觉得单身挺好 我都不敢谈恋爱了", "classification": "担忧、恐惧与焦虑情绪"},
    {"discussion": "太可怕啊", "classification": "担忧、恐惧与焦虑情绪"},
    {"discussion": "感觉比癌症可怕，因为身边人都怕感染会避嫌", "classification": "担忧、恐惧与焦虑情绪"},
    {"discussion": "要去广西上大学了怎么办", "classification": "担忧、恐惧与焦虑情绪"},

    # 幽默、戏谑与反讽表达
    {"discussion": "艾滋都能治 我痛风啥时候能啊", "classification": "幽默、戏谑与反讽表达"},
    {"discussion": "哈哈哈，你回答的有趣", "classification": "幽默、戏谑与反讽表达"},
    {"discussion": "艾滋：哥几个才来？", "classification": "幽默、戏谑与反讽表达"},
    {"discussion": "哈哈哈哈", "classification": "幽默、戏谑与反讽表达"}, # 视上下文，有时纯粹是幽默反应
    {"discussion": "我吴敬超实名跪下感谢大夫", "classification": "幽默、戏谑与反讽表达"}, # 夸张表达，带有戏谑

    # 疾病知识与传播讨论 (疑问/科普/辟谣)
    {"discussion": "高危是什么意思", "classification": "疾病知识与传播讨论 (疑问/科普/辟谣)"},
    {"discussion": "怎么才能知道自己得没得艾滋", "classification": "疾病知识与传播讨论 (疑问/科普/辟谣)"},
    {"discussion": "艾滋病是怎样的", "classification": "疾病知识与传播讨论 (疑问/科普/辟谣)"},
    {"discussion": "病毒离开肉体几秒就死了，根本不会传染的，没那么可怕的", "classification": "疾病知识与传播讨论 (疑问/科普/辟谣)"}, # 可能为错误科普或辟谣
    {"discussion": "真的不会空气传播和身体接触传播吗", "classification": "疾病知识与传播讨论 (疑问/科普/辟谣)"},

    # 信息来源与信任度讨论
    {"discussion": "全球最顶尖的医疗团队都没有治愈的方法，你想多了。", "classification": "信息来源与信任度讨论"},
    {"discussion": "前两天不是才公布说：全世界对于艾滋病疫苗的研究的最后一支实验也失败了嘛", "classification": "信息来源与信任度讨论"},
    {"discussion": "官方应该说明一下到底是不是真的。", "classification": "信息来源与信任度讨论"},
    {"discussion": "这又是要带什么节奏？", "classification": "信息来源与信任度讨论"},
    {"discussion": "卖疫苗的？", "classification": "信息来源与信任度讨论"},

    # 社会影响与公共议题探讨
    {"discussion": "这种能不能告对方给他判刑啊", "classification": "社会影响与公共议题探讨"},
    {"discussion": "把所有艾滋病人全部统计一下，让他们都去一个城市生活。", "classification": "社会影响与公共议题探讨"},
    {"discussion": "婚检真的是对自己负责", "classification": "社会影响与公共议题探讨"},
    {"discussion": "弄个艾康码，跟疫情的时候一样，谈恋爱前先拿出艾康码看一下", "classification": "社会影响与公共议题探讨"},
    {"discussion": "强烈支持公开", "classification": "社会影响与公共议题探讨"},

    # 风险轻视与认知偏差
    {"discussion": "艾滋病和癌症及心脑血管疾病相比，已经不算什么了。", "classification": "风险轻视与认知偏差"},
    {"discussion": "不影响生活，听说快能给治好l", "classification": "风险轻视与认知偏差"},
    {"discussion": "艾滋病其实就是超级癌症，定期体检，早查出来早治疗就是慢性病", "classification": "风险轻视与认知偏差"}, # 可能被解读为弱化其特殊性
    {"discussion": "得艾滋病会是啥情况", "classification": "风险轻视与认知偏差"}, # 若语气轻松，对严重性认知不足
    {"discussion": "艾滋病离体瞬间失去传染性", "classification": "风险轻视与认知偏差"}, # 如果用来泛指所有情况，可能导致风险认知偏差

    # 支持、鼓励与人文关怀
    {"discussion": "好孩子加油", "classification": "支持、鼓励与人文关怀"},
    {"discussion": "想开一点吧，", "classification": "支持、鼓励与人文关怀"},
    {"discussion": "心态一定要乐观 积极的治疗", "classification": "支持、鼓励与人文关怀"},
    {"discussion": "很勇敢，加油，好好生活，勇敢面对，一定要洁身自好", "classification": "支持、鼓励与人文关怀"},
    {"discussion": "小朋友，别听他们说的，事情已经发生，病情要紧，其他人的评论就是个屁，没有人比你重要！有病就去治，好好的啊", "classification": "支持、鼓励与人文关怀"},

    # 道德评判与归因指责
    {"discussion": "除了输血传染的其它的人不值得表扬", "classification": "道德评判与归因指责"},
    {"discussion": "风流过头折堕尾！", "classification": "道德评判与归因指责"},
    {"discussion": "你是不是胡搞了", "classification": "道德评判与归因指责"},
    {"discussion": "不自爱的结果。", "classification": "道德评判与归因指责"},
    {"discussion": "个人感觉得这病的都是不自重", "classification": "道德评判与归因指责"},

    # 其他/无法分类
    {"discussion": "学到了新知识！", "classification": "其他/无法分类"}, # 若非常泛指且无具体内容
    {"discussion": "评论区炸裂", "classification": "其他/无法分类"},
    {"discussion": "过来看评论", "classification": "其他/无法分类"},
    {"discussion": "这个适合转发给男朋友吗", "classification": "其他/无法分类"},
    {"discussion": "怎么不能下载呢？", "classification": "其他/无法分类"}
]

# 3. 定义消息模式 (MESSAGES_PATTERN)
MESSAGES_PATTERN = [
    {"role": "system", "content": """你是一个社交媒体评论分类助手。对于在分享艾滋病感染者生活日常的短视频平台上的评论，请根据评论的主要主题进行分类。注意：
1.每条评论只分配最主要的一个主题类别；
2.优先考虑评论的核心内容而非表面情绪；
3.注意识别评论中的深层含义、社会观念及对特定群体的态度"""},
    {
        "role": "user",
        "content": "以下是分类及其描述:\n{classifications}" # 将由 APIClassifier 动态填充
    },
    {
        "role": "user",
        "content": "请为以下这条关于“抗击艾滋病”的抖音评论分配一个最佳的主题类别，只需回复类别名称:\n\"\"\"\n{text}\n\"\"\"" # {text} 将被实际评论替换
    }
]


# --- 主程序 ---
async def main():
    # 请替换为您的实际 API 信息和文件路径
    API_URL = "url"  # 例如: "https://api.openai.com/v1/chat/completions"
    API_KEY = "your key"        # 您的API密钥

    if API_URL == "YOUR_LLM_API_ENDPOINT" or API_KEY == "sk-YOUR_API_KEY":
        print("请在脚本中配置您的 API_URL 和 API_KEY！")
        return

    classifier = APIClassifier(
        api_url=API_URL,
        api_key=API_KEY,
        classifications=CLASSIFICATIONS,
        messages_pattern=MESSAGES_PATTERN,
        # enable_thinking=True,
        model="DeepSeek-R1-671B", #  或者 "gpt-3.5-turbo", "gpt-4o-2024-08-06" 等您选择的模型
        temperature=0,         # 分类任务建议为0以保证一致性
        concurrency_limit=100   # 请根据您的API速率限制调整，100可能过高
    )

    # 请替换为您的实际输入CSV文件路径和包含评论的列名
    input_file = 'your_files'
    text_field_in_csv = 'AF' # 假设您的CSV中评论列名为 'comment_text'
    output_directory = 'output' # 输出目录
    # 确保输出目录存在
    import os
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print(f"开始处理文件: {input_file}，使用文本字段: '{text_field_in_csv}'")
    
    # 确保您的 APIClassifier 类中的 classify_single 方法已更新，
    # 如果未更新，EXAMPLES 参数虽然传递了，但可能不会在模型推理时被有效利用。
    output_path = await classifier.process_file(
        input_file=input_file,
        examples=EXAMPLES, # 传入示例
        text_field=text_field_in_csv,
        output_dir=output_directory
    )
    print(f"分类完成。结果已保存至: {output_path}")

if __name__ == "__main__":
    # 确保您的环境中安装了必要的库 (aiohttp, tenacity, tqdm)
    # pip install aiohttp tenacity tqdm
    asyncio.run(main())