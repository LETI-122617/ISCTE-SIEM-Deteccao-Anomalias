# Deteção de Anomalias e Redução de Falsos Positivos em Ambientes SIEM

**Mestrado em Engenharia de Telecomunicações e Informática**  
**Unidade Curricular:** Segurança em Redes e Sistemas de Informação  
**Instituição:** ISCTE - Instituto Universitário de Lisboa (2025/2026)

## 👥 Equipa e Docentes
**Autores:**
- Tomás Cerveira (122617)
- Alexandre Duarte (122657)
- Lara Machado (122655)
- Eduardo Real (122608)

**Docentes:** Daniel Pesqueira Morgado e Daniel Maximino Caçador

## 📖 Resumo do Projeto (Parte 1)
Este projeto aborda o problema da "fadiga de alertas" gerada pelo elevado volume de falsos positivos em Centros de Operações de Segurança (SOC). A Parte 1 (P-P1) propõe a substituição de regras analíticas baseadas em limites estáticos por modelos de deteção adaptativos baseados em estatística nativa (Média Móvel, Desvio Padrão Dinâmico e *Z-scores*). O trabalho foi suportado por uma Revisão Sistemática da Literatura (via plataforma Parsifal), evidenciando a viabilidade desta abordagem leve face à latência e custos computacionais de modelos complexos de *Machine Learning* e LLMs.

## 📂 Estrutura do Repositório

\`\`\`text
├── relatorio/                  # Documentação e Relatório P-P1
│   ├── main.tex                # Código fonte do relatório em LaTeX
│   ├── Deteccao_de_Anomalias_SIEM.pdf # Relatório final compilado
│   └── figuras/                # Imagens e gráficos utilizados no relatório
├── scripts/                    # Scripts desenvolvidos 
│   └── gerar_grafico_limiar.py # Script Python para geração do gráfico conceptual do limiar dinâmico
└── revisao_sistematica/        # Dados da extração e triagem metodológica
    ├── data_extraction.xls     # Tabela de extração de dados dos artigos
    └── parsifal_export.bib     # Exportação BibTeX dos estudos incluídos
\`\`\`

## 🛠️ Instruções de Compilação (LaTeX)
Para compilar o relatório a partir do código fonte:
1. Certifique-se de que possui uma distribuição LaTeX instalada (e.g., TeX Live, MiKTeX) ou utilize o Overleaf.
2. Na raiz da pasta `relatorio/`, execute o seguinte comando no terminal:
   \`\`\`bash
   pdflatex main.tex
   pdflatex main.tex
   \`\`\`
   *(Nota: O comando deve ser executado duas vezes consecutivas para garantir a correta geração do Índice e das Referências Cruzadas).*

## 🚀 Trabalhos Futuros (Parte 2)
Este repositório será atualizado futuramente para acomodar a **Parte 2 (P-P2)** do projeto, que incluirá:
- Implementação prática das *queries* nativas em ambiente SIEM (e.g., Splunk / Elastic Stack).
- Simulação de tráfego benigno e injeção de ataques de força bruta.
- Calibração empírica da constante de sensibilidade ($k$) e janela temporal ($N$).
- Validação através de métricas de desempenho (Matriz de Confusão, *F-Score*, FPR).
