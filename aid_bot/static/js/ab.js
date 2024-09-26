        async function sendMessage(event) {
            event.preventDefault();  // Prevent the form from submitting the traditional way

            const inputField = document.getElementById('sentence');
            const message = inputField.value;

            // Clear the input field after submission
            inputField.value = '';

            // Display the user's message in the chat window
            addMessageToChatWindow('You', message);

            // Send the message to the backend
            try {
                const response = await fetch('chat/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: JSON.stringify({ sentence: message })
                });

                const data = await response.json();

                if (response.ok) {
                    addMessageToChatWindow('Bot', data.response);
                } else {
                    addMessageToChatWindow('Error', 'Something went wrong. Please try again.');
                }
            } catch (error) {
                addMessageToChatWindow('Error', error);
            }
        }

        function addMessageToChatWindow(sender, message) {
            const chatWindow = document.getElementById('chat-window');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message';

            if (sender=="You"){
                messageDiv.className += ' user';
            }else{
                messageDiv.className += ' bot'
            }
            messageDiv.innerHTML = `${message}`;
            chatWindow.appendChild(messageDiv);
        }

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }