import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1=sentiment_analyzer("i love working with python")
        self.assertEqual(result_1['label'],'SENT_POSITIVE')
        result_2=sentiment_analyzer("i hate working with python")
        self.assertEqual(result_2['label'],'SENT_NEGATIVE')
        result_3=sentiment_analyzer("im neutral on python")
        self.assertEqual(result_3['label'],'SENT_NEUTRAL')

if __name__ == "__main__":
    unittest.main()