from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import random

class BlackjackApp(App):
    def build(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)
        self.player_score = self.deck.pop() + self.deck.pop()
        self.dealer_score = self.deck.pop() + self.deck.pop()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title = Label(text="🃏 Блэкджек 21 🃏", font_size=30, color=(1, 0.8, 0, 1))
        self.player_label = Label(text=f"Ваш счёт: {self.player_score}", font_size=20)
        self.dealer_label = Label(text="Счёт дилера: ?", font_size=20)
        self.result_label = Label(text="", font_size=24)

        layout.add_widget(self.title)
        layout.add_widget(self.player_label)
        layout.add_widget(self.dealer_label)
        layout.add_widget(self.result_label)

        btn_layout = BoxLayout(spacing=10)
        hit_btn = Button(text="Ещё", size_hint=(1, 0.5), background_color=(0, 0, 1, 1))
        stand_btn = Button(text="Хватит", size_hint=(1, 0.5), background_color=(0, 1, 0, 1))
        new_btn = Button(text="Новая", size_hint=(1, 0.5), background_color=(1, 0.6, 0, 1))

        hit_btn.bind(on_press=self.hit)
        stand_btn.bind(on_press=self.stand)
        new_btn.bind(on_press=self.new_game)

        btn_layout.add_widget(hit_btn)
        btn_layout.add_widget(stand_btn)
        btn_layout.add_widget(new_btn)

        layout.add_widget(btn_layout)

        return layout

    def hit(self, instance):
        card = self.deck.pop()
        self.player_score += card
        self.player_label.text = f"Ваш счёт: {self.player_score}"
        if self.player_score > 21:
            self.result_label.text = "Вы проиграли — перебор!"
            self.result_label.color = (1, 0, 0, 1)

    def stand(self, instance):
        while self.dealer_score < 17:
            self.dealer_score += self.deck.pop()
        self.dealer_label.text = f"Счёт дилера: {self.dealer_score}"

        if self.dealer_score > 21 or self.player_score > self.dealer_score:
            self.result_label.text = "Вы победили!"
            self.result_label.color = (0, 1, 0, 1)
        elif self.player_score == self.dealer_score:
            self.result_label.text = "Ничья!"
            self.result_label.color = (1, 0.6, 0, 1)
        else:
            self.result_label.text = "Вы проиграли!"
            self.result_label.color = (1, 0, 0, 1)

    def new_game(self, instance):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)
        self.player_score = self.deck.pop() + self.deck.pop()
        self.dealer_score = self.deck.pop() + self.deck.pop()
        self.player_label.text = f"Ваш счёт: {self.player_score}"
        self.dealer_label.text = "Счёт дилера: ?"
        self.result_label.text = ""


# Запуск приложения
BlackjackApp().run()