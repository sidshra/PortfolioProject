import { useState, useEffect } from 'react'

const URL = 'https://16jomruh80.execute-api.us-east-1.amazonaws.com/dev'

function App() {
  const [content, setContent] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(URL);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const json = await response.json();
        setContent(json); // Set the nested list state
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  },[])
  return (
    <>
      <div className='App'>
      Website content: {content}

      </div>
     
    </>
  )
}

export default App
