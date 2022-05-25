<template>
  <div>

	<!-- <div
		v-for="movie in nowMovies" :key="movie.id">
		{{movie.title}}
		{{movie.vote_average}}
		{{movie.release_date}}>
	</div>  -->
	<!-- v-model="test" -->
		<!-- <b-carousel-list  :data="nowMovies" :items-to-show="5">
			<template #item="list">
				<div class="card">
					<div class="card-image">
						<figure class="image ">
							<a @click="info(list.index)"><img :src="`https://image.tmdb.org/t/p/w500${list.poster_path}`" is-128x128></a>
						</figure>
						<b-tag type="is-danger" rounded style="position: absolute; top: 0;"><b>Now</b></b-tag>
						<b-tag type="is-dark" rounded style="position: absolute; bottom: 0;"><b>{{list.vote_average}}</b></b-tag>
					</div>
					<div class="card-content">
						<div class="content">
							<p class="title is-6">{{ list.title }}</p>
							<p class="subtitle is-7">{{ list.release_date }}</p>
						</div>
					</div>
				</div>
			</template>
		</b-carousel-list> -->

		<div class="container">
		<h1 class="title">NOW MOVIES</h1>

		<div class="row">
			<div v-for="movie in nowMovies" :key="movie.id" class="card col-2">
				<div class="card-image" id="cardimg">
					<figure class="image">
						<router-link :to="{ name: 'movie', params: {movieId: movie.id} }">
							<img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="movie poster" class=" is-128x128">
						</router-link>
					</figure>
				</div>
				<div class="card-content" id="cardcontent">
					
					<p>{{ movie.title }}</p>
					
					<p>{{ movie.release_date }}</p>
				</div>
			
			</div>
		</div>
  </div>
		<h1 class='title'>회원</h1>
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
		info(value) {
			this.test = value
		},
	},
	created(){
		this.fetchNowMovies()
	}
	
}

</script>
	
<style>
#cardimg{
	padding: auto;
	height:100px;
}
#cardcontent{
	padding: 0;
	height:100px;
}
</style>