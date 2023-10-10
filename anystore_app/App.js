import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
// imprting React WebView
import { WebView } from 'react-native-webview';

export default function App() {
  return (
    <WebView
      source={{ uri: 'https://www.anystoreweb.com' }}
      style={{ marginTop: 20 }}
    />

  );
}

