# This is a Gradio app that creates a chatbot capable of handling file uploads.
import gradio as gr

# Define a function to handle the chatbot's response.
def chatbot_response(message, history):
    # Append the user's message to the chat history.
    history.append({"role": "user", "content": message["text"]})
    
    # Process any files uploaded by the user.
    for file in message["files"]:
        history.append({"role": "user", "content": {"path": file}})
    
    # Generate a response from the chatbot.
    response = "I received your message and any files you sent."
    
    # Append the chatbot's response to the chat history.
    history.append({"role": "assistant", "content": response})
    
    return history

# Create a Gradio ChatInterface with a MultimodalTextbox for file uploads.
demo = gr.ChatInterface(
    fn=chatbot_response,
    type="messages",
    textbox=gr.MultimodalTextbox(
        placeholder="Type a message or upload a file...",
        file_count="multiple",
        sources=["upload", "microphone"],
    ),
    title="Multimodal Chatbot",
    description="Upload files and send messages to the chatbot.",
)

demo.launch(show_error=True)
