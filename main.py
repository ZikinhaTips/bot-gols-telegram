import requests
import time
import telegram

# === CONFIGURAÇÕES ===
TELEGRAM_TOKEN = '8081852578:AAFginPxtx3N6ET55nguz4QNqrgWqqn2SXc'
CHAT_ID = 924265477  # Substitua por seu ID real, se quiser personalizar

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def enviar_alerta(mensagem):
    bot.send_message(chat_id=CHAT_ID, text=mensagem)

def verificar_jogos():
    # Exemplo com dados simulados — substituiremos por API real depois
    jogos = [
        {"time_casa": "Time A", "time_fora": "Time B", "finalizacoes": 8, "ataques_perigosos": 60},
        {"time_casa": "Time C", "time_fora": "Time D", "finalizacoes": 2, "ataques_perigosos": 10},
    ]
    for jogo in jogos:
        if jogo["finalizacoes"] >= 5 and jogo["ataques_perigosos"] >= 50:
            mensagem = f"⚽ Jogo com bom ritmo:\n{jogo['time_casa']} x {jogo['time_fora']}\nFinalizações: {jogo['finalizacoes']}\nAtaques perigosos: {jogo['ataques_perigosos']}"
            enviar_alerta(mensagem)

while True:
    verificar_jogos()
    time.sleep(60)  # Verifica a cada 1 minuto
