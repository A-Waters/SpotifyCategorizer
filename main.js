const user = {
	authorized: false,
	access_token: null,
}

window.onload = () => {
	
	checkLogin();

	console.log(user.access_token);
	if(user.authorized) {
		fetch('https://api.spotify.com/v1/me', { headers: { Authorization: 'Bearer ' + user.access_token}})
		.then(response => {
			return response.json();
		})
		.then(me => {
			const elem = document.querySelector('#token');
			elem.innerHTML = `Hi, ${me.display_name}`
		});
	}

	
	document.querySelector('#redirect').onclick = redirect;
	
}

function redirect() {

		const client_id = 'fb37da23233d4fe581300fa8d7c4b3a0';
		const spotifyUrl = 'https://accounts.spotify.com/authorize';
		const redirect_uri = 'http://localhost:8000';
		const url = `${spotifyUrl}?client_id=${client_id}&response_type=token&redirect_uri=${redirect_uri}`
		window.location.href = url;
}

function checkLogin() {
	user.access_token = localStorage.getItem('access_token');
	if(user.access_token) {
		user.authorized = true;
	} else {
		const hashFrag = window.location.hash.substring(1);
		const urlParams = new URLSearchParams(hashFrag);
		const access_token = urlParams.get('access_token');
		if (access_token) {
			localStorage.setItem('access_token', access_token);
			user.access_token = access_token;
			user.authorized = true;
		}
	}
}