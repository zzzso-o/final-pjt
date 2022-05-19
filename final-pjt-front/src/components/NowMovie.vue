<template>
  <div>
		<!-- {{nowMovies}} -->
		<div 
    v-for="movie in nowMovies" :key="movie.id">
			{{movie.title}}
			{{movie.vote_average}}
			{{movie.release_date}}
			{{movie.poster_path}}
		</div>
			<!-- <b-carousel-list v-model="test" :data="nowMovies" :items-to-show="10">
				<template #item="list">
					<div class="card">
						<div class="card-image">
							<figure class="image is-5by4">
								<a @click="info(list.index)"><img :src="list.poster_path"></a>
							</figure>
							<b-tag type="is-danger" rounded style="position: absolute; top: 0;"><b>Now</b></b-tag>
						</div>
						<div class="card-content">
							<div class="content">
								<p class="title is-6">{{ list.title }}</p>
								<p class="subtitle is-7">{{ list.release_date }}</p>
								<b-field grouped >
										<p class="control" v-if="list.vote_average">
												<b-rate :value="list.vote_average" show-score disabled/>
										</p>
										<p class="control" style="margin-left: auto">
												<b-button size="is-small" type="is-danger" icon-left="heart" outlined />
										</p>
								</b-field>
							</div>
						</div>
					</div>
				</template>
			</b-carousel-list> -->

	</div>

	
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {

	computed: {
		...mapGetters(['nowMovies'])
	},

	methods:{
		...mapActions(['fetchNowMovies']),
		// info(value) {
		// 	this.test = value
		// }
	},
	created(){
		this.fetchNowMovies()
	}
	
}

</script>
	
<style>
	
</style>