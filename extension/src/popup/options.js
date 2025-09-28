const modelVersions = {
      gemini: [
        { id: 'gemini-2.5-flash', name: 'Gemini 2.5 Flash' },
        { id: 'gemini-2.5-pro', name: 'Gemini 2.5 Pro' },
        { id: 'gemini-1.5-pro', name: 'Gemini 1.5 Pro' }
      ],
      openai: [
        { id: 'gpt-5', name: 'GPT-5' },
        { id: 'gpt-4o', name: 'GPT-4o' },
        { id: 'gpt-4-turbo', name: 'GPT-4 Turbo' },
        { id: 'gpt-3.5-turbo', name: 'GPT-3.5 Turbo' }
      ]
    };

    function updateVersionDropdown() {
      const modelSelect = document.getElementById('aiModel');
      const versionSelect = document.getElementById('selectedVersion');
      const selectedModel = modelSelect.value;

      versionSelect.innerHTML = '';
      if (!selectedModel) {
        versionSelect.innerHTML = '<option value="">Select a provider first</option>';
        versionSelect.disabled = true;
        return;
      }

      versionSelect.disabled = false;
      versionSelect.innerHTML = '<option value="">Choose a version...</option>';
      modelVersions[selectedModel].forEach(v => {
        const option = document.createElement('option');
        option.value = v.id;
        option.textContent = v.name;
        versionSelect.appendChild(option);
      });
    }

    function saveSettings() {
      const model = document.getElementById('aiModel').value;
      const version = document.getElementById('selectedVersion').value;
      const apiKey = document.getElementById('apiKey').value;

      if (!model || !version || !apiKey) {
        alert('Please fill in all fields');
        return;
      }

      const settings = { model, version, apiKey, timestamp: new Date().toISOString() };
      console.log('Saving settings:', settings);

      const successMessage = document.getElementById('successMessage');
      successMessage.style.display = 'block';
      setTimeout(() => { successMessage.style.display = 'none'; }, 3000);
    }

    function resetSettings() {
      document.getElementById('aiModel').value = '';
      document.getElementById('selectedVersion').innerHTML = '<option value="">Select a provider first</option>';
      document.getElementById('selectedVersion').disabled = true;
      document.getElementById('apiKey').value = '';
    }