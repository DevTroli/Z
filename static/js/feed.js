document.addEventListener('DOMContentLoaded', () => {
  // Função para criar elementos dos zweets (mantida)
  function createZweetElement(zweet) {
    const div = document.createElement('div');
    div.className = 'bg-white p-4 m-2 rounded-lg shadow-md';
    div.innerHTML = `
      <div class="flex items-center m-2">
          <img src="${zweet.user.avatar_url}" 
               class="w-10 h-10 rounded-full mr-3">
          <span class="font-bold">${zweet.user.username}</span>
      </div>
      <p class="text-gray-800">${zweet.content}</p>
      <div class="mt-2 text-gray-500 text-sm">
          ${new Date(zweet.created_at).toLocaleString()} 
          · ${zweet.likes_count} curtidas
      </div>
    `;
    return div;
  }
});
