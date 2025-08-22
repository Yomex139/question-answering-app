with gr.Blocks() as app:
    gr.Markdown("# 📖 Question Answering Web App")
    gr.Markdown(
        "Paste a paragraph (context) and ask one or multiple questions.

"
        "✅ Interactive questions → get answers one-by-one
"
        "✅ Batch questions → enter multiple questions separated by newlines"
    )

    # Input: context
    context_input = gr.Textbox(label="Context", lines=6, placeholder="Paste your context paragraph here...")

    # ----- Interactive QA -----
    gr.Markdown("## 🤖 Interactive QA (One Question at a Time)")
    question_input = gr.Textbox(label="Question", placeholder="Ask a question about the context...")
    answer_output = gr.Textbox(label="Answer")
    confidence_output = gr.Textbox(label="Confidence Score")
    highlighted_output = gr.Textbox(label="Context with Highlighted Answer")
    
    interactive_btn = gr.Button("Get Answer")
    interactive_btn.click(
        single_inetractive_question,
        inputs=[context_input, question_input],
        outputs=[answer_output, confidence_output, highlighted_output]
    )

    # ----- Batch QA -----
    gr.Markdown("## 📄 Batch QA (Multiple Questions at Once)")
    batch_questions_input = gr.Textbox(label="Questions (one per line)", lines=5, placeholder="Enter multiple questions, each on a new line")
    batch_output = gr.Textbox(label="Answers")
    batch_btn = gr.Button("Get Batch Answers")
    batch_btn.click(multiple_interaction_questions, inputs=[context_input, batch_questions_input], outputs=batch_output)

# Launch app
app.launch()
