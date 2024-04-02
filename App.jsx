import { useState, useEffect } from 'react'

const URL = 'https://16jomruh80.execute-api.us-east-1.amazonaws.com/dev'

function App() {
  const [content, setContent] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetch(URL)
      result.json().then(json => {
        console.log(json)
      })
      
    }
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
