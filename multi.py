import concurrent.futures
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from textblob import TextBlob
import matplotlib.pyplot as plt


def complex_data_processing():
    """Demonstrate complex data processing with Pandas and NumPy"""
    print("\n=== Complex Data Processing ===")

    # Create a complex DataFrame
    dates = pd.date_range('20230101', periods=100)
    df = pd.DataFrame({
        'date': dates,
        'value': np.random.randn(100).cumsum(),
        'category': np.random.choice(['A', 'B', 'C', 'D'], 100)
    })

    # Perform complex operations
    df['rolling_avg'] = df['value'].rolling(window=7).mean()
    pivot = df.pivot_table(values='value', index=df['date'].dt.month, columns='category', aggfunc='mean')

    print("Pivot Table Summary:")
    print(pivot)

    # Visualize
    df.plot(x='date', y=['value', 'rolling_avg'], title='Time Series Analysis')
    plt.savefig('timeseries_plot.png')
    print("Saved time series plot to 'timeseries_plot.png'")


def machine_learning_task():
    """Demonstrate a machine learning workflow"""
    print("\n=== Machine Learning ===")

    # Load and prepare data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy:.2%}")
    print("Feature Importances:")
    for name, importance in zip(iris.feature_names, model.feature_importances_):
        print(f"{name}: {importance:.2%}")


def process_number(n):
    """Complex computation function (moved to module level)"""
    return sum(i * i for i in range(n) if i % 3 == 0 or i % 5 == 0)


def parallel_processing():
    """Demonstrate parallel processing"""
    print("\n=== Parallel Processing ===")

    numbers = [10000, 15000, 20000, 25000, 30000]

    # Sequential processing
    print("Starting sequential processing...")
    results_seq = [process_number(n) for n in numbers]

    # Parallel processing
    print("Starting parallel processing...")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results_par = list(executor.map(process_number, numbers))

    # Verify results
    assert results_seq == results_par
    print(f"Results verified - parallel processing successful!")
    print(f"Sample result for {numbers[0]}: {results_par[0]:,}")


def web_scraping_analysis():
    """Demonstrate web scraping and text analysis"""
    print("\n=== Web Scraping & NLP ===")

    # Scrape news headlines
    url = 'https://news.google.com/home?hl=en-US&gl=US&ceid=US:en'
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [h.text for h in soup.find_all('h3')[:10]]

        print("Latest News Headlines:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")

        # Sentiment analysis
        sentiments = [TextBlob(h).sentiment.polarity for h in headlines]
        avg_sentiment = sum(sentiments) / len(sentiments)

        print(f"\nAverage Sentiment Score: {avg_sentiment:.2f}")
        if avg_sentiment > 0.1:
            print("Overall Positive Sentiment")
        elif avg_sentiment < -0.1:
            print("Overall Negative Sentiment")
        else:
            print("Overall Neutral Sentiment")

    except Exception as e:
        print(f"Error during web scraping: {e}")


def image_processing():
    """Demonstrate complex image processing"""
    print("\n=== Image Processing ===")

    # Create a synthetic image
    width, height = 400, 400
    image = Image.new('RGB', (width, height))
    pixels = image.load()

    # Generate a complex pattern
    for x in range(width):
        for y in range(height):
            r = int((x ** 2 + y ** 2) % 256)
            g = int((x * y) % 256)
            b = int((x + y) * 2 % 256)
            pixels[x, y] = (r, g, b)

    # Apply filters and transformations
    image = image.filter(ImageFilter.GaussianBlur(radius=2))
    image = image.rotate(45, expand=True)

    # Save the image
    image.save('complex_image.png')
    print("Generated and processed complex image saved to 'complex_image.png'")


def main():
    """Orchestrate all complex tasks"""
    print("Starting Complex Python Program...\n")

    # Execute all tasks
    complex_data_processing()
    machine_learning_task()
    parallel_processing()
    web_scraping_analysis()
    image_processing()

    print("\nAll complex tasks completed successfully!")


if __name__ == "__main__":
    main()