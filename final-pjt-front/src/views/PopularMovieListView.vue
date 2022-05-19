<template>
  <div>
		<strong>POPULAR MOVIES</strong>

		<div 
    v-for="movie in popularMovies" :key="movie.id">
		{{movie.title}}
		{{movie.poster_path}}
		{{movie.release_date}}
		{{movie.vote_average}}
		
		
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