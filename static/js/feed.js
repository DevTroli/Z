document.addEventListener('DOMContentLoaded', () => {
  let page = 1;
  let loading = false;

  // Infinite Scroll
  window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 50 && !loading) {
      loadMoreZweets();
    }
  });

  async function loadMoreZweets() {
    loading = true;
    document.getElementById('loading').classList.remove('hidden');

    try {
      const response = await fetch(`/api/zweets/?page=${++page}`);
      const { results, next } = await response.json();

      const feed = document.getElementById('feed');
      results.forEach(zweet => {
        feed.appendChild(createZweetElement(zweet));
      });

      if (!next) window.removeEventListener('scroll');
    } catch (error) {
      console.error('Error loading zweets:', error);
    }

    loading = false;
    document.getElementById('loading').classList.add('hidden');
  }

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
