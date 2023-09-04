<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\BelongToMany;
use Illuminate\Database\Eloquent\HasMany;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Tymon\JWTAuth\Contructs\JWTSubject;

class User extends Authenticatable implements JWTSubject
{
    use HasFactory;
    protected $fileable = ['username','email','password','bio','images'];
    protected $visible = ['username','email','bio','image'];

    public function getRouteKeyName():string
   {
       return 'username';
   }

   public function article():HasMany
  {
       return $this->hasMany(Article::class);
  }

  public function favoriteArticles(): BelongsToMany
  {
      return  $this->belongsToMany(Article::class);
  }

  public function follower(): BelongssToMany
  {
       return  $this->belongsToMany(User::class, 'follower','follower_id','follower_id');
  }

  public function following(): BelongsToMany
  {
      return  $this->belongsToMany(User::class,'followers','follower_id','following_id');
  }

  public function doesUserFollowAnotherUser(int $followerId, int $followingId): bool
  {
      return  $this->where('id', $userId)->whereRelation('favoritedArticles','id', $articleId)->exists();
  }

  public function setPasswordAttribute(string $password): void
  {
      $this->attributes['password'] = bcrypt($password);
  }

  public function getJWTdentifier()
  {
      return  $this->getKey();
  } 

  public function getJWTCustomClaims()
  {
      return [];
  }
}
