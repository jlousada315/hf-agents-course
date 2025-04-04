# HF Agents Course

This repository contains code and examples for working with Hugging Face agents and different frameworks for building AI agents.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hf-agents-course.git
cd hf-agents-course
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Hugging Face API token:
```
HUGGINGFACE_API_TOKEN=your_token_here
```

## Project Structure

The project is organized into different directories, each focusing on a specific framework or approach:

- `llamaindex/`: Examples and implementations using the LlamaIndex framework
- `langgraph/`: Examples using the LangGraph framework for building agent workflows
- `smolagents/`: Examples using the SmolAgents framework for lightweight agent implementations

## Usage

Each directory contains its own set of examples and implementations. Navigate to the specific directory you're interested in and follow the instructions in the respective README files.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
