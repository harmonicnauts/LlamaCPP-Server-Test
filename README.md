# Llama.cpp test using OpenAI server

A test repo for running local Llama LLM model using Llama.cpp, OpenAI library, and streamlit as user interface.

# How to start?

1. Clone this repo : [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)
2. Run make commands (Windows)
   1. Download the latest fortran version of [w64devkit](https://github.com/skeeto/w64devkit/releases).
   2. Extract `w64devkit`.
   3. Run `w64devkit.exe`.
   4. Use the `cd` command to reach the `llama.cpp` folder.
   5. Run:
      ```bash
      make
      ```
3. Install these libraries

```bash
pip install openai 'llama-cpp-python[server]' pydantic instructor streamlit
```

4. Start the Llama.cpp server

- Run on CPU

```bash
python -m  llama_cpp.server --model ../models/the-file-name-of-your-model.ext
```

- Run on GPU

```bash
python -m  llama_cpp.server --model ../models/the-file-name-of-your-model.ext --n_gpu_layers {number of gpu layers}
```

### For more information and if you want to try using multimodal model. Go check out this video

[https://www.youtube.com/watch?v=voHTS9Nk5VY](https://www.youtube.com/watch?v=voHTS9Nk5VY)
