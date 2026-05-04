    const form = document.getElementById('contact-form');
    const responseMessage = document.getElementById('response-message');

    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        usrname: document.getElementById('usrname').value,
        password: document.getElementById('password').value,
      };

      try {
        const response = await fetch('https://script.google.com/macros/s/AKfycbyWDf2aN4mVK9RO-84G2aD3pD_rdKJyf4zOjP-OGFPUdxJF6UCeUUaHGeLzlK0A-ecm/exec', {
          method: 'POST',
          body: JSON.stringify(formData)
        });

        if (response.ok) {
          responseMessage.textContent = 'Thank you! Your message has been sent.';
          form.reset();
        } else {
          responseMessage.textContent = 'Error submitting the form. Please try again.';
        }
      } catch (error) {
        responseMessage.textContent = 'An error occurred. Please try again.';
      }
    });