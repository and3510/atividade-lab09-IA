"""
hyde.py — Passo 2
------------------
Recebe a query coloquial e usa um LLM local (sem API) para gerar
um documento hipotético técnico (HyDE).
"""

from transformers import pipeline


_generator = None


def _get_generator():
    global _generator
    if _generator is None:
        print("[Passo 2] Carregando modelo LLM local...")
        _generator = pipeline(
            "text-generation",
            model="facebook/opt-125m",
        )
    return _generator


def generate_hypothetical_document(query: str) -> str:
    print(f"\n[Passo 2] Query original: \"{query}\"")
    print("[Passo 2] Gerando documento hipotético via LLM local...")

    prompt = (
        f"Manual médico técnico. Sintoma relatado pelo paciente: {query}\n"
        f"Descrição clínica:"
    )

    generator = _get_generator()
    result = generator(prompt, max_new_tokens=80, do_sample=False)[0]["generated_text"]

    # Pega só o que veio depois do prompt
    doc = result[len(prompt):].strip()
    if not doc:
        doc = result.strip()

    print(f"[Passo 2] Documento hipotético gerado:\n  >> {doc}\n")
    return doc