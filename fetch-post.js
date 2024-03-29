const contentful = require('contentful');

// 環境変数からContentfulの設定を読み込む
const client = contentful.createClient({
  space: process.env.CONTENTFUL_SPACE_ID,
  accessToken: process.env.CONTENTFUL_ACCESS_TOKEN
});

client.getEntries({
  content_type: process.env.CONTENTFUL_CONTENT_TYPE_ID,
  order: '-fields.publishDate',
  limit: 5
})
.then((response) => {
  const posts = response.items.map((item) => {
    return `- [${item.fields.title}](YOUR_BLOG_URL/${item.fields.slug})`; // YOUR_BLOG_URLを実際のブログのURLに置き換える
  });
  console.log(posts.join('\n'));
})
.catch(console.error);
