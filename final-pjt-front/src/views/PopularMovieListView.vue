<template>

  <div class="container">
		<!-- {{popularMovies}} -->
		<h1 class="title">POPULAR MOVIES</h1>
		<div class="row">
			<div v-for="movie in popularMovies" :key="movie.id" class="card col-3">
				<div class="card-image">
					<figure >
						<router-link :to="{ name: 'movie', params: {movieId: movie.pk} }">
							<div>
								<img class="cropped" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="movie poster">
							</div>
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
.cropped {
	width: 180px; 
	height: 205px; 
	overflow: hidden;
}
	
</style>