import React, { useState, useEffect } from 'react';
import './App.css'; // Import CSS file for styling

const URL = 'https://16jomruh80.execute-api.us-east-1.amazonaws.com/dev';

function App() {
  const [content, setContent] = useState(null); // Set initial state to null

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(URL);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const json = await response.json();
        // Parse the nested list from the content string
        const nestedList = JSON.parse(json.content);
        setContent(nestedList); // Set the content state to the parsed nested list
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className='App'>
      <h1>Website content</h1>
      {/* Render content conditionally */}
      {content !== null ? (
        <div className="content-container">
          {/* Iterate over each item in the nested list */}
          {content.map((item, index) => (
            <div key={index} className="content-item">
              {/* Render image */}
              <img src={item[0]} alt={`Content Image ${index}`} className="content-image" />
              {/* Render headline with link */}
              <a href={item[2]} target='_blank' rel='noopener noreferrer'>
                <h2 className="content-headline">{item[1]}</h2>
              </a>
            </div>
          ))}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
