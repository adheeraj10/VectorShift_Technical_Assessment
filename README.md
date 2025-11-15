# 🚀 VectorShift - Frontend Technical Assessment

> An interactive workflow builder implemented with ReactFlow, Zustand, and FastAPI. This project allows users to visually design, connect, and run complex data pipelines, featuring a dynamic template-rendering engine and full backend validation.

<img width="1426" height="577" alt="image" src="https://github.com/user-attachments/assets/3b24479d-64a4-4c9f-b347-7a9c894538d9" />



---

## 🔧 Tech Stack

* **Frontend:** React, ReactFlow, Zustand
* **Backend:** Python, FastAPI
* **Styling:** Custom "Retro UI" Theme (CSS/Inline)
* **Core Logic:** Topological Sort (for DAG validation)

## 🎯 Core Features

* **Visual Workflow Canvas:** Drag-and-drop interface powered by ReactFlow.
* **Appealing "Retro UI" Theme:** A clean, color-coded, and professional design.
* **Unified Node Abstraction:** A single `NodeBase` component ensures a unified design and allows new nodes to be created efficiently.
* **10 Functional Nodes:**
    * `Input`: Provides initial data.
    * `Merge`: Combines two string inputs.
    * `Code`: A simple expression evaluator.
    * `Transform`: Maps input keys to output values.
    * `Delay`: Simulates an async operation.
    * `Banner`: Provides a static string output.
    * `Text`: A powerful template engine that dynamically creates handles for `{{variables}}` and renders a final string.
    * `LLM`: A mock node that previews the final prompt.
    * `Output`: A mock node that displays the final result.
* **Dynamic Template Hydration:** The `TextNode` automatically detects variables (including spaces, e.g., `{{Email category}}`) and pulls in data from connected nodes via a "Run" button.
* **Full Pipeline Validation:** Submits the graph to a Python backend to count nodes/edges and verify it's a Directed Acyclic Graph (DAG).
* **Global State Management:** Uses Zustand for a clean, hook-based approach to managing nodes, edges, and actions.

## 📁 Project Structure

```text
.
  backend/
    main.py           # FastAPI server with /pipelines/parse endpoint

  frontend/
    src/
      nodes/
        NodeBase.js       # The core node abstraction
        inputNode.js
        textNode.js       # Dynamic handle & template logic
        llmNode.js
        outputNode.js
        customNodes.js    # Banner, Code, Merge, Transform, Delay

      store.js            # Zustand global state
      ui.js               # ReactFlow canvas wrapper
      toolbar.js          # Draggable node toolbar
      submit.js           # Backend API submission logic
      App.js              # Root application

    package.json
    ...
```
## ▶️ Running the Project
1. Backend
First, navigate to the backend directory and start the FastAPI server.
```text
cd backend
uvicorn main:app --reload
```

The server will be running at http://localhost:8000.

2. Frontend
In a separate terminal, navigate to the frontend directory, install dependencies, and start the React app.

```text
cd frontend
npm install
npm start
```

The application will open in your browser at http://localhost:3000.

## ✨ Assessment Highlights

Clean Node Architecture: The NodeBase abstraction (Part 1) makes adding new, styled nodes trivial.
Robust Template Logic: The TextNode (Part 3) correctly parses variables, creates dynamic handles, and uses a "Run" button to reliably fetch and render data from all upstream sources.
Unified & Appealing Design: The "Retro UI" theme (Part 2) creates a professional, color-coded, and unified user experience.
End-to-End Integration: A complete, functional loop (Part 4) from the React UI to the Python backend (with a DAG check) and back to a user-friendly alert.

## 📌 Example Output
A complete connected pipeline, when "Run", generates a final rendered message in the TextNode's preview box, such as:

```text
Welcome to VectorShift!
User: Dheeraj A
Email category: Personal
System ready.
```

When the "Submit" button is pressed, the backend integration provides an alert:
```text
Pipeline parsed:
Nodes: 11
Edges: 9
Is DAG: true
```
