// import router from '@/router'
import axios from 'axios'
// import drf from '@/api/drf'
const API_DETAIL_URL = 'https://api.themoviedb.org/3/movie'
const API_URL = 'https://api.themoviedb.org/3/movie/popular'
const API_KEY = 'bd2e2aed22ef7bc837f34ff1cf7ef434'

const NOW_API_URL = 'https://api.themoviedb.org/3/movie/now_playing'
// const NOW_API_KEY = 'bd2e2aed22ef7bc837f34ff1cf7ef434'

// const today = new Date()
// const yesterday = new Date(today.setDate(today.getDate() -1)).toISOString().split("T")[0]
// const DATE = yesterday.replaceAll('-',"")
// 날짜를 하루전으로 해야 나옴 

// const SEARCH_URL = 'https://openapi.naver.com/v1/search/movie.json'
// const CLIENT_ID ='dgdluvp0gh93UPP2Tyyc'
// const CLIENT_SECRET = 'W7JqxZ40Rb'
// const searchKeyword = '영화'

export default {
	// state는 직접 접근
	state: {
		popularMovies: {}, 
		popularMovie :{},
		nowMovies: {},
		searchMovies: {},
		
	},
	// state는 getters 를 통해서 접근
	getters: {
		popularMovies: state => state.popularMovies,
		popularMovie: state => state.popularMovie,
		nowMovies: state => state.nowMovies,
		searchMovies: state => state.searchMovies,
	},
	
	mutations: {
		SET_POPULAR_MOVIES:(state, popularMovies) => state.popularMovies = popularMovies,
		SET_POPULAR_MOVIE:(state, popularMovie) => state.popularMovie = popularMovie,
		SET_NOW_MOVIES:(state, nowMovies) => state.nowMovies = nowMovies,
		SET_SEARCH_MOVIES:(state, searchMovies) => state.searchMovies = searchMovies,

	},

	actions: {
		fetchPopularMovies({ commit }){
			axios
			.all([
				axios.get(`${API_URL}/?api_key=${API_KEY}&language=ko&page=1`),
				axios.get(`${API_URL}/?api_key=${API_KEY}&language=ko&page=2`),
				axios.get(`${API_URL}/?api_key=${API_KEY}&language=ko&page=3`),
				axios.get(`${API_URL}/?api_key=${API_KEY}&language=ko&page=4`),
				axios.get(`${API_URL}/?api_key=${API_KEY}&language=ko&page=5`),
			])
			.then(axios.spread((res1, res2, res3, res4, res5) => 
				{
					const data1 = res1.data.results;
          const data2 = res2.data.results;
          const data3 = res3.data.results;
          const data4 = res4.data.results;
					const data5 = res5.data.results;
					const res = [...data1, ...data2, ...data3, ...data4, ...data5];
					commit('SET_POPULAR_MOVIES', res)
				})
			)
			.catch(err => { // 실패시 에러메시지
					console.error(err.response.data)
			})
		},

		fetchPopularMoive({ commit }, moviePk){
			
			axios
			.get(`${API_DETAIL_URL}/${moviePk}?api_key=${API_KEY}&language=ko`)
			.then(res => { // 성공시에 
				commit('SET_POPULAR_MOVIE', res.data)
			})
			.catch(err => { 
				console.error(err.response.data)
			})
		},

		fetchNowMovies({ commit }){
			axios
			.get(`${NOW_API_URL}/?api_key=${API_KEY}&language=ko-kr`)
			.then(res => { // 성공시에 
					commit('SET_NOW_MOVIES', res.data.results)
			})
			.catch(err => { 
					console.error(err.response.data)
			})
		},

		// 네이버 영화 검색 

		// fetchSearchMovies({ commit }){
		// 	axios.get(`${SEARCH_URL}`,{
		// 		params:{
		// 			query:searchKeyword,
		// 			display: 100
		// 		},
		// 		headers:{
		// 			'X-Naver-Client-Id': CLIENT_ID,
		// 			'X-Naver-Client-Secret': CLIENT_SECRET
		// 		}
		// 	})
		// 	.then(res => { // 성공시에 
		// 			commit('SET_SEARCH_MOVIES', res.data)
		// 	})
		// 	.catch(err => { 
		// 			console.error(err.response.data)
		// 	})
		// },

		

	},
}
