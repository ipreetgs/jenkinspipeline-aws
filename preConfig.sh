text=$(cat << EOF
AWS_SECRETKEY=
AWS_ACCESSKEY=
EOF
)

echo "$text" >credentials
