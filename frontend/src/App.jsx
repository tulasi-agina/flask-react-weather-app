// App.jsx - React frontend for sending a city name to a Flask backend and displaying the temperature

import { useState } from 'react'  // useState is a React hook for managing component state

function App() {
  // Declare state variables for the user input and the server's response
  const [input, setInput] = useState('')
  const [response, setResponse] = useState('')

  // Function to send the input to Flask backend and handle the response
  const sendMessage = async () => {
    try {
      // Send POST request to Flask at /api/message with user input
      const res = await fetch(import.meta.env.VITE_API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: input })
      })

      // Parse the JSON response from Flask and update the response state
      const data = await res.json()
      setResponse(data.response)
    } catch (err) {
      // Log any error and show a fallback message
      console.error('Error:', err)
      setResponse('Error connecting to Flask backend')
    }
  }

  // Render the UI: input box, send button, and response display
  return (
    <div style={{ padding: '2rem' }}>
      <h1>React + Flask App</h1>

      {/* User input field for city name */}
      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Enter a city name (e.g. Seattle)"
      />

      {/* Send Button to send the input to Flask */}
      <button onClick={sendMessage} style={{ marginLeft: '1rem' }}>
       Check Temperature
      </button>

      {/* Display the response from Flask */}
      <p>{response}</p>
    </div>
  )
}

export default App  // Export the component s
