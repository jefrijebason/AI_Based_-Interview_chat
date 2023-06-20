import openai
import gradio as gr


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

input1= gr.inputs.Textbox(placeholder="OPENAI KEY")
openai.api_key = input1
outputs = gr.outputs.Textbox(label="Reply")

def update_textbox(input1):
    input1.visible=False

gr.Interface(fn=chatbot, inputs=[input1,inputs], outputs=outputs, title="IntiAI Chatbot",
             description="Ask Interview related questions.",
             theme="compact",on_submit=update_textbox).launch(share=True)