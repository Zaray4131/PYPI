import gradio as gr


def greet(name):
  return f"Hello, {name}!"


# Create the Gradio interface
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Launch the app
if __name__ == "__main__":
  demo.launch()

