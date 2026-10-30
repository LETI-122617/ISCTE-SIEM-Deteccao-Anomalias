"""
Script de Geração do Gráfico Conceptual de Limiar Adaptativo (Z-Score)
Projeto: Deteção de Anomalias em Ambientes SIEM
Mestrado ETI - ISCTE-IUL
"""

import numpy as np
import matplotlib.pyplot as plt

def gerar_grafico():
    # 1. Configuração da semente para reprodutibilidade
    np.random.seed(42)
    tempo = np.arange(0, 50)
    
    # 2. Gerar tráfego normal (ruído benigno com média 20 e desvio padrão 3)
    trafego_normal = 20 + np.random.normal(0, 3, 50)
    
    # 3. Inserir anomalia: Ataque de Força Bruta no instante t=35
    eventos = trafego_normal.copy()
    eventos[35] = 85  # Pico anómalo
    
    # 4. Cálculo simplificado da baseline e do limiar (mu + 3*sigma)
    media_movel = np.full(50, 20) 
    limiar = media_movel + (3 * 3) # Assumindo sigma aproximado de 3
    
    # 5. Plot do gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(tempo, eventos, label='Eventos de Autenticação ($X_t$)', color='#1f77b4', marker='o', markersize=4)
    plt.plot(tempo, limiar, label='Limiar Adaptativo ($\mu + 3\sigma$)', color='#d62728', linestyle='--')
    
    # 6. Anotações
    plt.annotate('Ataque de Força Bruta\n(Alerta Disparado)', 
                 xy=(35, 85), xytext=(20, 75),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                 fontsize=10, fontweight='bold')
    
    # 7. Formatação
    plt.title('Deteção de Anomalias via Desvio Padrão Dinâmico', fontsize=14)
    plt.xlabel('Tempo ($t$)', fontsize=12)
    plt.ylabel('Volume de Eventos Falhados', fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    
    # 8. Guardar e mostrar
    plt.savefig('grafico_limiar.png', dpi=300)
    print("Gráfico 'grafico_limiar.png' gerado com sucesso!")

if __name__ == "__main__":
    gerar_grafico()
