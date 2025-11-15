🚀 VectorShift Frontend Technical Assessment

Interactive Workflow Builder (ReactFlow + FastAPI)

This project implements a visual workflow builder where users can drag nodes, connect them, transform data, render templates, and view a final output. The system demonstrates full-stack capability across UI engineering, state management, and backend validation.

.
├── backend/
│   └── main.py               # FastAPI backend (pipeline parser + DAG validation)
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── nodes/
    │   │   ├── NodeBase.js
    │   │   ├── inputNode.js
    │   │   ├── textNode.js
    │   │   ├── llmNode.js
    │   │   ├── outputNode.js
    │   │   └── customNodes.js   # Banner, Code, Transform, Merge, Delay
    │   ├── store.js
    │   ├── ui.js
    │   ├── toolbar.js
    │   ├── draggableNode.js
    │   ├── submit.js
    │   └── App.js
    ├── index.css
    └── index.js

⸻

🔧 Tech Stack

Frontend: React, ReactFlow, Zustand, Custom Nodes, Retro UI Theme
Backend: FastAPI, Topological Sort (DAG validation)
Other: Modular architecture, clean component structure, template rendering engine

⸻

🎯 Core Features
	•	Drag-and-drop workflow canvas
	•	Eight functional custom nodes:
	•	Input
	•	Merge
	•	Code (expression evaluator)
	•	Transform (CSV mapping)
	•	Delay
	•	Banner
	•	Text (template + variable resolver)
	•	LLM (preview generator)
	•	Output
	•	Dynamic Text template system ({{variable}} hydration)
	•	Fully working LLM preview flow
	•	Pipeline submission to backend
	•	DAG validation + structured response
	•	Retro-styled visual node theme

⸻

📁 Project Structure
backend/
  main.py                # FastAPI pipeline parser

frontend/
  src/
    nodes/               # All custom node implementations
      NodeBase.js
      inputNode.js
      textNode.js
      llmNode.js
      outputNode.js
      customNodes.js
    store.js             # Zustand global state
    ui.js                # Canvas + ReactFlow wrapper
    toolbar.js           # Draggable node toolbar
    submit.js            # API submission logic
    App.js               # Root application

▶️ Running the Project

Backend
cd backend
uvicorn main:app --reload

Frontend
cd frontend
npm install
npm start


📌 Example Output

A complete connected pipeline generates a final message such as:
Welcome to VectorShift!
User: Dheeraj A
Email category: Personal
System ready.


✨ Highlights
	•	Clean, modular node architecture
	•	Well-structured UI with reusable NodeBase
	•	Custom variable resolution logic
	•	End-to-end frontend + backend integration
	•	Professional UX polish with a retro theme
