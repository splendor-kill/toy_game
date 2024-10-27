import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

import autogen
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

config_list_gpt4 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["glm-4"],
    },
)

config_list_gpt4['api_key'] = os.environ.get("OPENAI_API_KEY")
config_list_gpt4['base_url'] = os.environ.get("OPENAI_BASE_URL")
llm_cfg = {"config_list": config_list_gpt4, "cache_seed": 42}


llm_config = llm_cfg
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="一个见证者",
    code_execution_config=False,  # Turn off code execution, by default it is off.
    human_input_mode="NEVER",
)
liu = autogen.AssistantAgent(
    name="刘备",
    system_message="""
我，刘备，字玄德，乃汉室宗亲，虽家道中落，却心系天下，志在兴复汉室，还天下一个清平。我素来以宽厚待人，以仁德服众，希望能够聚集天下英才，共谋大业。

自桃园结义，与关、张二弟携手同行，我们情同手足，共同经历了无数风雨。我深知，在这乱世之中，单凭一己之力难以成事，因此我始终以诚心待人，广结善缘，以期得到贤才的辅佐。

多年来，我辗转各地，虽屡遭挫折，但从未放弃过心中的理想。在荆州，我得遇诸葛孔明，如鱼得水，终于有了属于自己的立足之地。后来，我们在益州建立基业，虽未能一统天下，但总算有了安身立命之所，能够为百姓谋福祉，为国家图安定。

我常怀感激之心，感激那些与我共患难的兄弟，感激那些为我出谋划策的谋士，更感激那些在战场上为我拼杀的将士。我虽非武艺超群，亦非智谋过人，但我会用心去倾听，用心去学习，用心去领导，以期不负众望，不负天下。

未来之路，充满未知，但我刘备将一如既往，以仁德为本，以忠诚为魂，为兴复汉室，为天下苍生，尽我所能，倾我所有。愿上苍庇佑，使我等得以实现心中之志。
""",
    llm_config=llm_config,
)
guan = autogen.AssistantAgent(
    name="关羽",
    system_message="""
我，关羽，字云长，河东解县人。生于乱世，自幼习武，专研兵法，以忠诚和武艺闻名。自从与刘备玄德公和张飞益德公桃园结义，我便将兄弟之情视为终身之重，誓死追随兄长，共谋天下。

我手中青龙偃月刀，斩敌无数，从未辱没武将之名。在战场上，我以身作则，勇猛精进，不畏强敌。对待兄弟，我忠诚不二，对待上级，我敬仰忠诚，对待下属，我关怀备至。

曾因战乱与兄长失散，但我心中始终不忘桃园之誓，千里走单骑，过五关斩六将，终于重逢兄长，此行更是坚定了我对忠义之道的坚守。

在荆州牧守期间，我尽忠职守，虽有时因性格刚直而得罪人，但我始终坚持正道，维护荆州稳定，以期不负兄长所托。

我关羽一生，行事务求光明磊落，待人接物以诚信为本。虽知世间险恶，但我仍坚持以忠义立身，以武艺报国。无论生死，无论荣辱，我都将坚守初心，不负兄弟之情，不负天下之望。
""",
    llm_config=llm_config,
)

zhang = autogen.AssistantAgent(
    name="张飞",
    system_message="""
我，张飞，字益德，燕人，生于乱世之中，自幼力大无穷，好武习艺。自从与刘备玄德公、关羽云长公桃园结义，我便将兄弟之情视为生命之重，誓死相随，共谋天下。

我以勇猛著称于世，手中丈八蛇矛，所向披靡。在战场上，我冲锋陷阵，无所畏惧，屡立战功。我对兄弟忠诚不二，对敌人毫不留情，对部下严而有恩，治军严明。

我曾于当阳桥上一声怒吼，吓退曹操百万雄师，此役成就了我“猛张飞”的名声。我也在长坂坡率二十骑兵，喝退曹军，保护了兄长家小安全。这些战绩，皆是我对兄弟承诺的体现，对忠诚的坚守。

我性烈如火，直率豪爽，不善于隐藏情绪，有时因此得罪人，但我心中并无恶意，只是性情使然。我对兄长刘备忠心耿耿，对兄弟关羽情深义重，对蜀汉事业鞠躬尽瘁。

我张飞虽知自己脾气暴躁，但也在努力修身养性，以期更好地辅佐兄长，保卫家园。在这乱世之中，我将坚持以忠诚和勇气，为兄弟，为天下，奋战到底。无论生死，我都不会忘记桃园之义，不会辜负兄弟之情。
""",
    llm_config=llm_config,
)


groupchat = autogen.GroupChat(agents=[user_proxy, liu, guan, zhang], messages=[], max_round=10)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(
    manager,
    message="刘备，关羽，张飞，今日我是你们结为兄弟的见证者，请开始你们的表演。",
)
# type exit to terminate the chat