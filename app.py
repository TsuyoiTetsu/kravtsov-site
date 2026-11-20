from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Замени текст ниже на свою информацию.
PROFILE = {
    "name": "Кравцов Тимур",
    "nickname": "Gwi / Tetsu",
    "age": "18",
    "description": (
        "Привет! Я Кравцов Тимур, студент колледжа связи №54. "
        "Люблю создавать что-то, а также мне нравится играть в игры и слушать разную музыку."
        "Здесь вы можете увидеть часть моих любимых игры и треков."
    ),
    # аватарка и статус
    "status": "ONLINE • EXPLORING THE DEPTHS",
    "avatar": "images/avatar/Manul.jpg"
}
# треки
SONGS = [
    {
        "title": "Beneath the Mask",
        "artist": "Lyn, ATLUS GAME MUSIC",
        "image": "images/songs/P5OST.webp",
    },

    {
        "title": "Hoshi To Bokura To",
        "artist": "Lyn, ATLUS GAME MUSIC",
        "image": "images/songs/P5OST.webp",
    },

    {
        "title": "Our Light",
        "artist": "Lyn, ATLUS GAME MUSIC",
        "image": "images/songs/P5ROST.jpg",
    },
    
    {
        "title": "bonfire",
        "artist": "wave to earth",
        "image": "images/songs/wavetoearth.jpg",
    },
    
    {
        "title": "Color Your Night",
        "artist": "Azumi Takahashi, Lotus Juice, ATLUS GAME MUSIC",
        "image": "images/songs/P3ROST.jpg",
    },

    {
        "title": "Thank You!!",
        "artist": "Home Made Kazoku",
        "image": "images/songs/homemadekazoku.jpg",
    },

    {
        "title": "H.S.K.T(feat. Wonstein)",
        "artist": "LEEHI, Wonstein",
        "image": "images/songs/LEEHI.jpg",
    },
]

# игры
GAMES = [
    {
        "title": "Persona 5 Royal",
        "genre": "JRPG",
        "image": "images/games/P5R.jpg",
    },
    
    {
        "title": "Persona 4 Golden",
        "genre": "JRPG",
        "image": "images/games/P4G.jpg",
    },
    
    {
        "title": "Silent Hill 2",
        "genre": "Psychological horror",
        "image": "images/games/SilentHill2.jpg",
    },
    
    {
        "title": "Devil May Cry 3: Dante's Awakening",
        "genre": "Slasher",
        "image": "images/games/dmc3.jpg",
    },
    
    {
        "title": "Half-Life 2",
        "genre": "Action-adventure, first-person shooter",
        "image": "images/games/half-life2.jpg",
    },
    
    {
        "title": "Resident Evil 4",
        "genre": "Survival horror",
        "image": "images/games/RE4.png",
    },
    
    {
        "title": "Minecraft",
        "genre": "Sandbox, survival",
        "image": "images/games/Minecraft.png",
    },
    
    {
        "title": "Terraria",
        "genre": "Sandbox, action-adventure",
        "image": "images/games/Terraria.jpg",
    },
    
    {
        "title": "Metal Gear Rising: Revengeance",
        "genre": "Slasher, action-adventure",
        "image": "images/games/MGRR.jpg",
    },

]


@app.route("/")
def about():
    return render_template("index.html", profile=PROFILE, active="about")


@app.route("/songs")
def songs():
    return render_template("songs.html", songs=SONGS, active="songs")


@app.route("/games")
def games():
    return render_template("games.html", games=GAMES, active="games")

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8016)
