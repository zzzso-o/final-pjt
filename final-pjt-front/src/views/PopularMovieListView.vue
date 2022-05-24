<template>
  <div class="container">
		<h1 class="title">POPULAR MOVIES</h1>
		<div class="row">
			<div v-for="movie in popularMovies" :key="movie.id" class="card col-3">
				<div class="card-image">
					<figure class="image">
						<router-link :to="{ name: 'movie', params: {movieId: movie.id} }">
							<img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="movie poster" class=" is-128x128">
						</router-link>
					</figure>
				</div>
				<div class="card-content">
					<div class="media">
						<p class="title is-5">{{ movie.title }}</p>
					</div>
					<p>{{ movie.release_date }}</p>
				</div>
				<footer class="card-footer">
					<p class="card-footer-item">
						<span>
							<router-link :to="`popular/${movie.id}`"></router-link>
						</span>
					</p>
				</footer>
			</div>
		</div>
  </div>
	
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
	data() {
		return {
			items : [],
			current:1,
			perPage:12,
			rangeBefore: 5,
			rangeAfter: 5,
			order: 'is-centered',
			size: '',
			isSimple: false,
			isRounded: false,
			hasInput: false,
			inputPosition: '',
			inputDebounce: '',

		}
	},
	computed: {
    ...mapGetters(['popularMovies']),
		// total(){
		// 	return this.$store.getters['popularMovies'].length
		// },
		// paginatedItems(){
		// 	let page_number = this.current-1
		// 	return this.$store.getters['popularMovies'].slice(page_number * this.perPage, (page_number+1) * this.perPage)
		// }
  },

	methods:{
		...mapActions(['fetchPopularMovies'])
	},
	created(){
		this.fetchPopularMovies()
		// this.items.push('popularMovies')		
	}

	
}

</script>
	
<style>

	
</style>