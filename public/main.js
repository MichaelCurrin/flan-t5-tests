const BASE_URL = "https://api-inference.huggingface.co/models"

async function query(payload, token, modelId) {
  console.log("Requesting API")

  const response = await fetch(`${BASE_URL}/${modelId}`, {
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(payload),
  });

  return await response.json();
}


function storeInputs(token, modelId, prompt) {
  localStorage.setItem('huggingFaceToken', token);
  localStorage.setItem('huggingFaceModelId', modelId);
  localStorage.setItem('huggingFacePrompt', prompt);
}

function loadStoredInputs() {
  console.log('Setting form inputs from local storage')
  const storedToken = localStorage.getItem('huggingFaceToken');
  const storedModelId = localStorage.getItem('huggingFaceModelId');
  const storedPrompt = localStorage.getItem('huggingFacePrompt');

  if (storedToken) {
    document.getElementById('token').value = storedToken;
  }
  if (storedModelId) {
    document.getElementById('modelId').value = storedModelId;
  }
  if (storedPrompt) {
    document.getElementById('prompt').value = storedPrompt;
  }
}

function displayResponse(response) {
  const responseElement = document.getElementById('response');

  console.debug(response)

  if (!(response)) {
    responseElement.textContent = "ERROR: No response received.";
    return
  }

  if (response.error) {
    responseElement.textContent = `ERROR: ${response.error}`
    return
  }

  if (response[0].generated_text) {
    responseElement.textContent = response[0].generated_text;
    return
  }

  responseElement.textContent = "ERROR: Unexpected error.";
}


document.getElementById('form').addEventListener('submit', async (event) => {
  event.preventDefault();

  const token = document.getElementById('token').value;
  const modelId = document.getElementById('modelId').value;
  const prompt = document.getElementById('prompt').value;
  const responseElement = document.getElementById('response');

  storeInputs(token, modelId, prompt);

  responseElement.textContent = "Loading...";

  try {
    const response = await query({ "inputs": prompt }, token, modelId);
    displayResponse(response);
  } catch (error) {
    responseElement.textContent = "Error: " + error.message;
  }
});

document.addEventListener('DOMContentLoaded', loadStoredInputs);
