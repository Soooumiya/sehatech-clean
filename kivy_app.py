from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.webview import WebView  # Webview for mobile app

class SehaTechNewApp(App):
    def build(self):
        # Replace this with the URL of your deployed Streamlit app
        return WebView(url='https://your-username.streamlit.app')

if __name__ == '__main__':
    SehaTechNewApp().run()
