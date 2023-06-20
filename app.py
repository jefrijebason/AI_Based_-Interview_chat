import openai
import gradio as gr

openai.api_key = "...."

messages = [
    {"role": "system", "content": "You are an AI specialized in solving Interview questions and tips to cracking them.Do not answer anything other than Interview-related queries."},
]
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with Interview AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="IntiAI Chatbot",
             description="Ask Interview related questions.",
             theme="compact").launch(share=True)