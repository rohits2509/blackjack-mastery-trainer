# Blackjack Mastery Trainer

A simple Python command-line game to help you memorize and master blackjack basic strategy. It randomly generates hands and quizzes you on the correct move: **Hit**, **Stand**, **Double**, or **Split**.

## 🎯 Purpose
To accelerate your learning of blackjack strategy through repetition and immediate feedback.

---

## 🛠 Features
- Random hand generation (hard, soft, pair)
- Strategy suggestion based on a predefined chart
- Immediate feedback on your decisions

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/blackjack-mastery-trainer.git
cd blackjack-mastery-trainer
```

### 2. Run the Trainer
```bash
python blackjack_trainer.py
```

---

## 📂 File Structure
```
blackjack-mastery-trainer/
├── blackjack_trainer.py      # Main game loop
├── strategy_chart.py         # Basic strategy rules
├── utils.py                  # Card handling utilities
├── README.md                 # Project info and usage
└── data/
    └── history_log.csv       # (Optional) Answer history log
```

---

## 🧠 How It Works
Each round, you're dealt a random hand and the dealer shows one card. The script will ask you to choose your move and compare it against the correct strategy.

---

## ✅ To Do
- Add history tracking and scoring
- Expand full strategy chart coverage
- Export incorrect moves to CSV

---

## 📘 Resources
- [Basic Blackjack Strategy Chart](https://www.blackjackapprenticeship.com/blackjack-strategy-charts/)
- [Blackjack Wikipedia](https://en.wikipedia.org/wiki/Blackjack)

---

## 📄 License
MIT License
