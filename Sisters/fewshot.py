import asyncio
from api_class import APIClassifier # 确保您的 APIClassifier 类保存在此文件中
                                        # 并且 classify_single 方法已修改为可以使用 few-shot EXAMPLES
                                        # (如我上一个回复中建议的那样)

# --- 配置区域 ---

# 1. 定义分类标准 (CLASSIFICATIONS)
#    这些分类是基于“精神小妹生活方式和现象”的初步建议，您可以根据需要调整。
CLASSIFICATIONS = {
    "外貌与装扮": "评论主要讨论精神小妹的妆容、发型、衣着风格、声音、体型等外在特征。",
    # "Appearance & Style": "Comments focusing on the makeup, hairstyle, clothing style, voice, or physique of 'spiritual little sisters'.",

    "行为与生活方式": "评论主要描述或评价其日常行为、消费习惯、娱乐方式（如爱玩、昼伏夜出）、生活态度（如不爱学习、及时行乐）。",
    # "Behavior & Lifestyle": "Comments describing or evaluating their daily actions, spending habits, entertainment choices, and attitudes (e.g., playful, disinterest in studies, hedonistic).",

    "社会评价与观念": "评论主要表达对精神小妹群体的正面/负面看法、社会影响、刻板印象、道德评判或支持。",
    # "Social Perception & Opinion": "Comments expressing positive/negative views, societal impact, stereotypes, moral judgments, or support for the 'spiritual little sister' group.",

    "情感与人际关系": "评论主要讨论精神小妹的恋爱观、友情、家庭关系，或其提供/索取的情绪价值。",
    # "Relationships & Emotional Value": "Comments on their views on love, friendships, family relations, or the emotional value they provide/seek.",

    "真实性与表演性质": "评论主要质疑相关视频内容的真实性，是否为剧本、摆拍，或为了博取关注的表演。",
    # "Authenticity & Performance": "Comments questioning the authenticity of video content, suspecting it's scripted, staged, or a performance for attention.",

    "地区与群体特征": "评论主要提及特定地区与精神小妹现象的关联，或讨论该群体的某些共同区域性或亚文化特征。",
    # "Regional & Group Characteristics": "Comments linking the phenomenon to specific regions or discussing shared characteristics of this subculture.",

    "个人经历分享": "评论者主要分享自己与精神小妹/小伙相关的亲身经历、故事或观察。",
    # "Personal Anecdotes": "Commenters sharing their personal experiences, stories, or observations related to 'spiritual little sisters/brothers'.",

    "寻求互动与模仿": "评论者主要表达想认识精神小妹、询问如何模仿其风格、寻求一起参与其活动或表达想成为其中一员。",
    # "Seeking Interaction & Imitation": "Commenters expressing a desire to meet, imitate, or join 'spiritual little sisters', or asking for information about them.",

    "其他": "不属于以上任何类别的评论，如纯表情符号、无关话题、过于简短无法判断或无法分类的零散内容。",
    # "Other": "Comments not fitting into any above categories, such as pure emojis, unrelated topics, too short to classify, or miscellaneous content."
}

# 2. 定义示例 (EXAMPLES)
#    从您提供的评论中选取或构造一些清晰的例子。
#    确保 'discussion' 包含评论文本，'classification' 包含对应的 CLASSIFICATIONS 中的中文键名。
EXAMPLES = [
    # 外貌与装扮
    {"discussion": "精神小妹的声音都是一样的", "classification": "外貌与装扮"},
    {"discussion": "我看了好久以为黑丝那个是男的", "classification": "外貌与装扮"},
    {"discussion": "为了瘦我要当精神小妹了", "classification": "外貌与装扮"},

    # 行为与生活方式
    {"discussion": "他们并不坏，只是喜欢玩而已", "classification": "行为与生活方式"},
    {"discussion": "边走边吃边扔垃圾，就这么把素质丢在地上了？", "classification": "行为与生活方式"},
    {"discussion": "该读书的年龄不好好读书 现在只能吃生活的苦 这是每个人的选择", "classification": "行为与生活方式"},

    # 社会评价与观念
    {"discussion": "虽然大家批评这俩精神小妹，但是一般身边这种性格的是混的最好的", "classification": "社会评价与观念"},
    {"discussion": "从头到尾都是不良导向！！！抖音的后台瞎了！！！！", "classification": "社会评价与观念"},
    {"discussion": "符合我对这个群体印象 不读书喜欢混搞孤立搞霸凌年纪小小 性成熟的比成年人都开放", "classification": "社会评价与观念"},

    # 情感与人际关系
    {"discussion": "情绪价值满满的，请这200让我花", "classification": "情感与人际关系"},
    {"discussion": "其实我挺喜欢精神小妹，感觉她们很需要被保护，又是恋爱脑，又纯情又专一", "classification": "情感与人际关系"},
    {"discussion": "恋爱脑来了 玫瑰", "classification": "情感与人际关系"},

    # 真实性与表演性质
    {"discussion": "这么多好看的真的假的", "classification": "真实性与表演性质"},
    {"discussion": "应该是剧本吧 不能这样吧", "classification": "真实性与表演性质"},
    {"discussion": "这是专门拍摄效果？", "classification": "真实性与表演性质"},
    
    # 地区与群体特征
    {"discussion": "长得确实山东", "classification": "地区与群体特征"},
    {"discussion": "很符合我对河南的刻板印象 流泪真的只是刻板印象没有不好的意思", "classification": "地区与群体特征"},
    {"discussion": "贵账号是我了解河南的唯一途径", "classification": "地区与群体特征"},

    # 个人经历分享
    {"discussion": "谈过 除了朋友圈喜欢自拍加文案 有点符文 其他都挺好的 超听话 又容易满足 又水嫩 看", "classification": "个人经历分享"},
    {"discussion": "我高中时候有个室友，一个月600块钱生活费，花450买耐克的鞋", "classification": "个人经历分享"},
    {"discussion": "我当初也是黄毛 妹子也是一叫一堆 现在都各自奔波了", "classification": "个人经历分享"},

    # 寻求互动与模仿
    {"discussion": "问题来了去哪找精神小妹", "classification": "寻求互动与模仿"},
    {"discussion": "我A2000带我玩玩", "classification": "寻求互动与模仿"},
    {"discussion": "哥我出五百让我演一集行吗", "classification": "寻求互动与模仿"},

    # 其他
    {"discussion": "笑死我了", "classification": "其他"},
    {"discussion": "精神小妹", "classification": "其他"}, # 简单提及，未展开
    {"discussion": "不知道怎么说了", "classification": "其他"}
]

# 3. 定义消息模式 (MESSAGES_PATTERN)
MESSAGES_PATTERN = [
    {
        "role": "system", 
        "content": """你是一个社交媒体评论分类助手。请根据用户提供的关于“精神小妹”生活方式和现象的抖音评论，依据其主要主题进行分类。请注意：
1. 每条评论只分配最主要的一个主题类别。
2. 优先考虑评论的核心内容和潜在含义，而不仅仅是表面情绪或个别词汇。
3. 注意识别评论中可能存在的网络用语、梗、反讽或隐晦表达。"""

# You are a social media comment classification assistant. For Douyin comments about the 'spiritual little sister' (精神小妹) lifestyle and phenomenon, please categorize them based on their main theme. Note:
# 1. Each comment should be assigned only one primary category.
# 2. Prioritize the core content and potential underlying meaning over surface emotions or isolated words.
# 3. Pay attention to internet slang, memes, irony, or subtle expressions within the comments."""
    },
    {
        "role": "user",
        "content": "以下是分类及其描述:\n{classifications}" # 将由 APIClassifier 动态填充
    },
    {
        "role": "user",
        "content": "请为以下这条关于“精神小妹”的抖音评论分配一个最佳的主题类别，只需回复类别名称:\n\"\"\"\n{text}\n\"\"\"" # {text} 将被实际评论替换
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
