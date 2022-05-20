<template>
  <div>
		<h1 class='title'>POPULAR MOVIES</h1>
		
		<div class="columns">
		<div 
    v-for="movie in popularMovies" :key="movie.id">
		<!-- {{movie.title}}

		{{movie.release_date}}
		{{movie.vote_average}} -->
		
		
		<div class="card column">
			<div class="card-image">
				<figure class="image ">
				<img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="movie poster" class=" is-128x128">
				</figure>
			</div>
			<div class="card-content">
				<div class="media">
				<div class="media-content">
					<p class="title is-5">{{movie.title}}</p>
				</div>
				</div>
				<br>
				<time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
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

		<template>
		<section>
			<b-pagination
					:total="total"
					v-model="current"
					:range-before="rangeBefore"
					:range-after="rangeAfter"
					:order="order"
					:size="size"
					:simple="isSimple"
					:rounded="isRounded"
					:per-page="perPage"
					:page-input="hasInput"
					:page-input-position="inputPosition"
					:debounce-page-input="inputDebounce">
			</b-pagination>
    </section>
		</template>
  </div>
	
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
	data() {
		return {
				total: 100,
				current: 5,
				perPage: 20,
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
    ...mapGetters(['popularMovies'])
  },

	methods:{
		...mapActions(['fetchPopularMovies'])
	},
	created(){
		this.fetchPopularMovies()
		
	}
	
}

</script>
	
<style>
	
</style>