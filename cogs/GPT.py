# from discord.ext.commands import Cog, command
# from transformers import AutoTokenizer
# import transformers
# import torch
# from dotenv import dotenv_values
# from llama2 import Llama2
#
#
# config = dotenv_values("data.env")
#
#
# class GPT(Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self.token = config["LLAMA_TOKEN"]
#         llama = Llama2('YOUR_LLAMA2_API_KEY')
#
#     @Cog.listener()
#     async def on_ready(self):
#         print("GPT => Ready")
#
#     @command(name="gpt")
#     async def gpt(self, ctx):
#         msg = ctx.message.content.split(">gpt ")
#         model = "meta-llama/Llama-2-7b-chat-hf"
#         tokenizer = AutoTokenizer.from_pretrained(model)
#         pipeline = transformers.pipeline(
#             "text-generation",
#             model=model,
#             torch_dtype=torch.float16,
#             device_map="auto",
#         )
#         sequences = pipeline(
#             f'{msg[1]}\n',
#             do_sample=True,
#             top_k=10,
#             num_return_sequences=1,
#             eos_token_id=tokenizer.eos_token_id,
#             max_length=200,
#         )
#         print(sequences)
#         for seq in sequences:
#             await ctx.reply(seq['generated_text'])
#
#
# async def setup(bot):
#     await bot.add_cog(GPT(bot))
